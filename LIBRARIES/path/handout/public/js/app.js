// Vienna Hacking Bootcamp - Client-side JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add loading states to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (this.getAttribute('href') && !this.getAttribute('href').startsWith('#')) {
                this.classList.add('loading');
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Loading...';
                
                // Reset after navigation or timeout
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.classList.remove('loading');
                }, 2000);
            }
        });
    });
});

// Refresh files function
function refreshFiles() {
    const button = event.target.closest('button');
    const originalText = button.innerHTML;
    
    button.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Refreshing...';
    button.disabled = true;
    
    // Reload the page after a short delay
    setTimeout(() => {
        window.location.reload();
    }, 500);
}

// File operations
const FileManager = {
    // Copy file URL to clipboard
    copyFileUrl: function(fileName) {
        const url = `${window.location.origin}/view?file=${encodeURIComponent(fileName)}`;
        navigator.clipboard.writeText(url).then(() => {
            this.showNotification('File URL copied to clipboard!', 'success');
        }).catch(err => {
            console.error('Failed to copy URL: ', err);
            this.showNotification('Failed to copy URL', 'error');
        });
    },
    
    // Show notifications
    showNotification: function(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show position-fixed`;
        notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
        notification.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'} me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto-remove after 3 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 3000);
    }
};

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K for search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        // Focus on search input if exists
        const searchInput = document.querySelector('input[type="search"]');
        if (searchInput) {
            searchInput.focus();
        }
    }
    
    // Escape to go back
    if (e.key === 'Escape') {
        // If on view page, go back to files
        if (window.location.pathname === '/view') {
            window.location.href = '/files';
        }
    }
});

// Enhanced file viewing
if (window.location.pathname === '/view') {
    // Add line numbers to code content
    const fileContent = document.getElementById('fileContent');
    if (fileContent) {
        const lines = fileContent.textContent.split('\n');
        const numberedContent = lines.map((line, index) => {
            return `${(index + 1).toString().padStart(3, ' ')} | ${line}`;
        }).join('\n');
        
        // Only add line numbers if content is not too long
        if (lines.length < 1000) {
            fileContent.textContent = numberedContent;
        }
    }
}