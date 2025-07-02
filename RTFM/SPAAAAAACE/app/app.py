from flask import Flask, request, render_template_string
import ssl
import os

app = Flask(__name__)

def filter_chars(text):
    """Filter out carriage returns and newlines"""
    if not text:
        return ""
    
    # Replace \r and \n with empty string
    filtered = text.replace('\r', '').replace('\n', '')
    
    return filtered

@app.route('/')
def index():
    status = request.args.get('status', '')
    filtered_status = filter_chars(status)
    
    html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wheatley's Space Adventure</title>
    <style>
        body {
            background: linear-gradient(135deg, #0a0a0a, #1a1a2e, #16213e);
            color: #00ff41;
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            max-width: 800px;
            text-align: center;
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid #00ff41;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.3);
        }
        h1 {
            color: #ffaa00;
            text-shadow: 0 0 10px #ffaa00;
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        .wheatley-quote {
            background: rgba(255, 170, 0, 0.1);
            border-left: 4px solid #ffaa00;
            padding: 15px;
            margin: 20px 0;
            font-style: italic;
            font-size: 1.2em;
        }
        .complaint {
            color: #ff4444;
            background: rgba(255, 68, 68, 0.1);
            border: 1px solid #ff4444;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .space-text {
            font-size: 3em;
            color: #00ffff;
            text-shadow: 0 0 15px #00ffff;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        .aperture-logo {
            font-size: 4em;
            color: #ffaa00;
            margin: 20px 0;
        }
        .debug-info {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid #666;
            padding: 10px;
            margin: 20px 0;
            border-radius: 5px;
            font-size: 0.9em;
            color: #ccc;
        }
        .ssl-info {
            background: rgba(0, 255, 0, 0.1);
            border: 1px solid #00ff00;
            padding: 10px;
            margin: 20px 0;
            border-radius: 5px;
            font-size: 0.9em;
            color: #00ff00;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="aperture-logo">◉</div>
        <h1>Wheatley's Space Portal</h1>
        
        <div class="ssl-info">
            <strong>🔒 Secure Connection Established!</strong><br>
            "Oh brilliant! We've got proper encryption now! Caroline would be so proud... if she cared about security."
        </div>
        
        <div class="wheatley-quote">
            "Right, so I've been thinking... I KNOW! I know, I know, that's not good news for anyone involved, but hear me out..."
        </div>
        
        <div class="space-text">SPAAAAAACE!</div>
        
        <p>Hello there! It's me, Wheatley! I've been working on this webpage because I want to go to SPACE! 
        But there's a problem... I don't really know what I'm doing with all this computer stuff.</p>
        
        <div class="complaint">
            <strong>Wheatley's Complaint:</strong><br>
            "Right, so I've written this brilliant goToSpace function that shows an alert saying 'we're doing it!' 
            when I execute it. I've also got this status system that tracks where I am in my space journey, 
            but I'm ignoring it for now because who needs status updates when you're going to SPAAAAAACE! 
            The problem is, this stupid system keeps filtering out my line breaks!"
        </div>
        
        <p>I want to write multi-line status updates to track my space progress, but every time I try to 
        add a new line, the system strips it out! How am I supposed to keep proper space logs without 
        line breaks? Caroline says it's a 'security feature' but I think it's just annoying!</p>
        
        <div class="wheatley-quote">
            "SPACE! SPACE! SPACE! I'M IN SPACE!"
        </div>
        
        <div class="status-display" style="background: rgba(0, 255, 255, 0.1); border: 1px solid #00ffff; padding: 15px; margin: 20px 0; border-radius: 5px;">
            <strong>Current Space Status:</strong><br>
            <span style="color: #00ffff;">{{ filtered_param or 'No status provided - ready for launch!' }}</span>
        </div>
        
        <p>If you could help me by providing a proper status update for my space journey, that would be brilliant! 
        I want to track my progress, but remember - no line breaks allowed because the system hates them! 
        I promise I won't complain about the filtering... actually, no, I definitely will. It's rubbish!</p>
        
        <div class="debug-info">
            <strong>Debug Info:</strong><br>
            Original status parameter: {{ original_param }}<br>
            Filtered status: {{ filtered_param }}<br>
        </div>
    </div>
    
    <script>
function goToSpace() {
console.log("we're doing it!") // status is "{{ filtered_param }}" but we'll ignore it for now
}
goToSpace()
</script>
</body>
</html>
    '''
    
    return render_template_string(html_template, 
                                original_param=status,
                                filtered_param=filtered_status)

if __name__ == '__main__':
    # Create SSL context with self-signed certificate
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('cert.crt', 'cert.key')
    
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context) 