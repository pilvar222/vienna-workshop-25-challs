# Vienna Hacking Bootcamp - File Sharing Platform

🛡️ **Secure File Sharing Platform**

A secure file sharing platform for the Vienna Hacking Bootcamp with advanced security features.

## Overview

This platform provides a secure file sharing system for the Vienna Hacking Bootcamp training program. The application implements multiple layers of security including path sanitization, access controls, and input validation to ensure safe file access.

## Features

- **Secure File Access**: Advanced path sanitization prevents unauthorized file access
- **User-Friendly Interface**: Modern, responsive web interface built with Bootstrap 5
- **File Management**: Browse and view shared training materials
- **Access Controls**: Restricted file access within designated directories
- **Monitoring**: Comprehensive logging and security monitoring

## Deployment

### Using Docker

1. Build the container:
```bash
docker build -t vienna-hacking-bootcamp .
```

2. Run the container:
```bash
docker run -p 3000:3000 vienna-hacking-bootcamp
```

### Using Docker Compose

```bash
docker-compose up -d
```

### Manual Setup

1. Install dependencies:
```bash
npm install
```

2. Start the application:
```bash
npm start
```

3. Access the application at `http://localhost:3000`

## Usage

### Accessing the Platform
1. Navigate to the homepage to see the platform overview
2. Use the "Shared Files" section to browse available training materials
3. Click "View" to read any file content
4. Use the copy function to share file contents with other participants

### Security Features
- **Path Sanitization**: All file paths are sanitized to prevent unauthorized access
- **Directory Restrictions**: File access is limited to the designated shared directory
- **Input Validation**: All user inputs are validated and filtered
- **Error Handling**: Comprehensive error handling with user-friendly messages

### File Management
- Browse available training materials and documentation
- View file contents in a clean, readable format
- Copy file contents for sharing or reference
- All file access is logged for security monitoring

## Technical Details

- **Node.js/Express** web application
- **EJS** templating engine
- **Bootstrap 5** for styling
- **Advanced Security**: Multiple layers of protection against common web vulnerabilities

## Security Architecture

- **Input Sanitization**: All user inputs are properly sanitized and validated
- **Path Security**: Advanced path sanitization prevents directory traversal
- **Access Controls**: Strict file access controls within designated directories
- **Error Handling**: Secure error handling prevents information disclosure

---

*Vienna Hacking Bootcamp - Secure File Sharing Platform* 