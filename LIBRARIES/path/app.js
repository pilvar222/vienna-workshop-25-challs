const express = require('express');
const path = require('path');
const fs = require('fs');
const sanitize = require('path-sanitizer');

const app = express();
const PORT = process.env.PORT || 3000;

// Set up EJS as template engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files
app.use('/static', express.static(path.join(__dirname, 'public')));

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Application directory where shared files are stored
const APP_DIR = path.join(__dirname, 'shared_files');

// Ensure shared files directory exists
if (!fs.existsSync(APP_DIR)) {
    fs.mkdirSync(APP_DIR, { recursive: true });
}

// Routes
app.get('/', (req, res) => {
    res.render('index');
});

app.get('/about', (req, res) => {
    res.render('about');
});

app.get('/files', (req, res) => {
    try {
        const files = fs.readdirSync(APP_DIR);
        res.render('files', { files });
    } catch (error) {
        res.render('files', { files: [], error: 'Could not read files directory' });
    }
});

// Secure file viewer endpoint with path sanitization
app.get('/view', (req, res) => {
    const fileName = req.query.file;
    
    if (!fileName) {
        return res.status(400).render('error', { 
            message: 'No file specified',
            details: 'Please provide a file parameter' 
        });
    }

    try {
        // Sanitize the file path to prevent directory traversal attacks
        const sanitizedPath = sanitize(fileName);
        const filePath = path.join(APP_DIR, sanitizedPath);
        

        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                return res.status(404).render('error', { 
                    message: 'File not found',
                    details: `Could not read file: ${fileName}` 
                });
            }
            
            res.render('view', { 
                fileName: fileName,
                content: data,
                sanitizedPath: sanitizedPath 
            });
        });
        
    } catch (error) {
        res.status(500).render('error', { 
            message: 'Server error',
            details: error.message 
        });
    }
});

// API endpoint for file listing (for AJAX requests)
app.get('/api/files', (req, res) => {
    try {
        const files = fs.readdirSync(APP_DIR);
        res.json({ files });
    } catch (error) {
        res.status(500).json({ error: 'Could not read files' });
    }
});

// 404 handler
app.use((req, res) => {
    res.status(404).render('error', { 
        message: 'Page not found',
        details: 'The requested page does not exist' 
    });
});

// Error handler
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).render('error', { 
        message: 'Something went wrong!',
        details: 'An unexpected error occurred' 
    });
});

app.listen(PORT, () => {
    console.log(`🚀 Vienna Hacking Bootcamp Platform running on port ${PORT}`);
    console.log(`📁 Shared files directory: ${APP_DIR}`);
}); 
