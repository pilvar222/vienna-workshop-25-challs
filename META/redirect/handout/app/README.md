# SVG Animation Studio - XSS Challenge

This is a CTF challenge demonstrating an XSS vulnerability through SVG attribute injection in a `<set>` tag.

## Setup

### Using Docker (Recommended)

1. Build the container:
```bash
docker build -t svg-xss-challenge .
```

2. Run the container:
```bash
docker run -p 5000:5000 svg-xss-challenge
```

3. Access the application at `http://localhost:5000`

### Manual Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access the application at `http://localhost:5000`

## The Vulnerability

The application allows users to customize SVG animations by setting various parameters. User input is directly inserted into the attributes of an SVG `<set>` tag without proper sanitization.

**Vulnerable code location**: The `<set>` tag in the HTML template where user input is inserted as attributes:

```html
<set attributeName="fill" to="{{ to_color }}" dur="{{ duration }}" repeatCount="{{ repeat_count }}" {{ extra_attrs|safe }} />
```

## Injection Points

You can inject arbitrary attributes through any of these form fields:
- Animation Duration
- From Color  
- To Color
- Repeat Count

The vulnerability allows you to:
- Break out of existing attribute values using quotes
- Inject new attributes into the `<set>` tag
- Potentially achieve XSS depending on your payload

## Example Test

Try entering something like this in the "Animation Duration" field:
```
2" onbegin="alert('XSS')"
```

This will close the `dur` attribute and inject an `onbegin` event handler.

## Goal

Use the attribute injection to achieve XSS execution in the context of the SVG element. 