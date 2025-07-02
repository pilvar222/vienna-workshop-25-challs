from flask import Flask, request, render_template_string, make_response
import html

app = Flask(__name__)

# HTML template for Vienna Hacking Bootcamp 2025
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vienna Hacking Bootcamp 2025 - Welcome Portal</title>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Vienna Hacking Bootcamp 2025 🚀</h1>
            <div class="subtitle">Elite Cybersecurity Training Program</div>
            <div class="vienna-flag">🇦🇹</div>
        </div>

        <!-- HTML Injection Point - User message displayed without escaping -->
        <div class="welcome-message">
            <h2>Welcome Message</h2>
            {{ user_message | safe }}
        </div>

        <div class="form-section">
            <h3>🎯 Participant Portal</h3>
            <p>Customize your welcome message for the bootcamp!</p>
            
            <form method="GET">
                <div class="form-group">
                    <label for="message">Your Welcome Message:</label>
                    <input type="text" id="message" name="message" value="{{ message_param }}" 
                           placeholder="Enter your personalized welcome message...">
                </div>
                <button type="submit" class="btn">Update Portal</button>
            </form>
        </div>

        <div class="form-section">
            <h3>🍪 Session Information</h3>
            <p>Your current session cookies (from HTTP headers):</p>
            <div class="cookie-display">
                <h3>Browser Cookies:</h3>
                <div>{{ cookie_data | safe }}</div>
            </div>
        </div>

        <div class="hacker-ascii">
    ██╗   ██╗██╗███████╗███╗   ██╗███╗   ██╗ █████╗ <br/>
    ██║   ██║██║██╔════╝████╗  ██║████╗  ██║██╔══██╗<br/>
    ██║   ██║██║█████╗  ██╔██╗ ██║██╔██╗ ██║███████║<br/>
    ╚██╗ ██╔╝██║██╔══╝  ██║╚██╗██║██║╚██╗██║██╔══██║<br/>
     ╚████╔╝ ██║███████╗██║ ╚████║██║ ╚████║██║  ██║<br/>
      ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝<br/>
             HACKING BOOTCAMP 2025
        </div>

        <div class='footer'>
            <p>🛡️ Advanced Penetration Testing & Ethical Hacking 🛡️</p>
            <p>Vienna, Austria • January 2025 • Secure. Learn. Hack.</p>
        </div>
    </div>


</body>
</html>
'''.replace('\n', '')

@app.route('/', methods=['GET'])
def index():
    # Get the message parameter - this will be vulnerable to HTML injection
    message_param = request.args.get('message', '')
    
    # Create vulnerable user message by directly inserting without escaping
    if message_param:
        user_message = f"<p>🎉 <strong>Personal Message:</strong> {message_param}</p>"
    else:
        user_message = "<p>👋 Welcome to the Vienna Hacking Bootcamp 2025! Please enter your welcome message above.</p>"
    
    # Read cookies from HTTP request headers (server-side)
    cookies = request.cookies
    if cookies:
        cookie_list = []
        for cookie_name, cookie_value in cookies.items():
            cookie_list.append(f"<strong>{cookie_name}:</strong> {cookie_value}")
        cookie_data = "<br>".join(cookie_list)
    else:
        cookie_data = "<em>No cookies found in this session.</em>"
    
    # Create response with strict CSP
    response = make_response(render_template_string(
        HTML_TEMPLATE,
        user_message=user_message,
        message_param=message_param,
        cookie_data=cookie_data
    ))
    
    # Add strict Content Security Policy
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) 