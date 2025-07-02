from flask import Flask, request, render_template_string
import html

app = Flask(__name__)

# HTML template with SVG containing vulnerable set tag
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SVG Animation Studio</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 { color: #333; text-align: center; }
        .form-group { margin: 15px 0; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select { 
            width: 100%; 
            padding: 8px; 
            border: 1px solid #ddd; 
            border-radius: 4px; 
        }
        button {
            background: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover { background: #0056b3; }
        .preview {
            border: 1px solid #ddd;
            padding: 20px;
            margin-top: 20px;
            border-radius: 4px;
            background: #fafafa;
        }
        svg { border: 1px solid #ccc; background: white; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 SVG Animation Studio</h1>
        <p>Create custom SVG animations by adjusting the parameters below!</p>
        
        <form method="GET">
            <div class="form-group">
                <label for="duration">Animation Duration (seconds):</label>
                <input type="text" id="duration" name="duration" value="{{ duration }}" placeholder="2">
            </div>
            
            <div class="form-group">
                <label for="from_color">From Color:</label>
                <input type="text" id="from_color" name="from_color" value="{{ from_color }}" placeholder="#ff0000">
            </div>
            
            <div class="form-group">
                <label for="to_color">To Color:</label>
                <input type="text" id="to_color" name="to_color" value="{{ to_color }}" placeholder="#0000ff">
            </div>
            
            <div class="form-group">
                <label for="repeat_count">Repeat Count:</label>
                <input type="text" id="repeat_count" name="repeat_count" value="{{ repeat_count }}" placeholder="indefinite">
            </div>
            
            <button type="submit">Generate Animation</button>
        </form>
        
        {% if duration %}
        <div class="preview">
            <h3>Preview:</h3>
            <svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
                <rect width="100" height="100" x="150" y="50" fill="{{ from_color }}">
                    <!-- VULNERABLE: User input directly inserted as attributes -->
                    <set attributeName="fill" to="{{ to_color }}" dur="{{ duration }}" repeatCount="{{ repeat_count }}" {{ extra_attrs }} />
                </rect>
                <text x="200" y="180" text-anchor="middle" font-family="Arial" font-size="14">
                    Animated Rectangle
                </text>
            </svg>
        </div>
        {% endif %}
        
        <div style="margin-top: 30px; padding: 15px; background: #e9ecef; border-radius: 4px;">
            <h3>About this tool:</h3>
            <p>This SVG Animation Studio allows you to create custom color transitions for shapes. 
               Perfect for prototyping animations for web projects!</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    # Get parameters from the query string, with sensible defaults
    duration = request.args.get('duration', '')
    from_color = request.args.get('from_color', '')
    to_color = request.args.get('to_color', '')
    repeat_count = request.args.get('repeat_count', '')
    extra_attrs = request.args.get('extra_attrs', '')

    return render_template_string(
        HTML_TEMPLATE,
        duration=duration,
        from_color=from_color,
        to_color=to_color,
        repeat_count=repeat_count,
        extra_attrs=extra_attrs
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) 