// Force puppeteer to store everything to /tmp/
process.env.HOME = "/tmp";

const { delay, handleTargetCreated, handleTargetDestroyed, logMainInfo, logMainError } = require("./utils");
const puppeteer = require("puppeteer");

// Banner
const tips = ["Every console.log usage on the bot will be sent back to you :)", "There is a small race window (~10ms) when a new tab is opened where console.log won't return output :("];
console.log(`==========\nTips: ${tips[Math.floor(Math.random() * tips.length)]}\n==========`);

// Restrict access to a specific domain of a TLD.
const PAC_B64 = Buffer.from(`
function FindProxyForURL (url, host) {
	if (host == "challenge-name.fcsc.fr") return "DIRECT";
	if (host.endsWith("fcsc.fr")) return "PROXY 127.0.0.1:1";
	return "DIRECT";
}
`).toString("base64");

// Spawn the bot and navigate to the user provided link.
async function goto(url) {
	logMainInfo("Starting the browser...");
	const browser = await puppeteer.launch({
		headless: "new",
		ignoreHTTPSErrors: true,
		args: [
			"--no-sandbox",
			"--disable-gpu",
			"--disable-jit",
			"--disable-wasm",
			"--disable-dev-shm-usage",
			`--proxy-pac-url=data:application/x-ns-proxy-autoconfig;base64,${PAC_B64}`,
			'--ignore-certificate-errors'
		],
		executablePath: "/usr/bin/chromium-browser"
	});

	// Hook tabs events
	browser.on("targetcreated", handleTargetCreated.bind(browser));
	browser.on("targetdestroyed", handleTargetDestroyed.bind(browser));

	/* ** CHALLENGE LOGIC ** */
	const [page] = await browser.pages(); // Reuse the page created by the browser.
	await handleTargetCreated(page.target()); // Since it was created before the event listener was set, we need to hook it up manually.
	await page.setDefaultNavigationTimeout(5000);

	logMainInfo("Setting cookie...");
	// VIENNA CHALLENGE SPECIFIC START
	try { await page.goto('https://challenge/') } catch(error) {
		console.log(error);
	}
	await delay(1000);
	await page.setCookie({
		name: "flag",
		value: "vienna{https://www.youtube.com/watch?v=BVn1oQL9sWg}",
		domain: "challenge",
		path: "/",
		httpOnly: false,
		secure: false,
	});
	// VIENNA CHALLENGE SPECIFIC END
	logMainInfo("Going to the user provided link...");
	try { await page.goto(url) } catch(error) {
		console.log(error);
	}
	await delay(5000);

	logMainInfo("Leaving o/");
	await browser.close();
	return;
}

// Handle TCP data
process.stdin.on("data", (data) => {
	const url = data.toString().trim();

	if (!url || !(url.startsWith("http://") || url.startsWith("https://"))) {
		logMainError("You provided an invalid URL. It should start with http:// or https://.");
		process.exit(1);
	}

	goto(url)
	.then(() => process.exit(0))
	.catch((error) => {
		if (process.env.ENVIRONMENT === "development") {
			console.error(error);
		}
		process.exit(1);
	});
});