#!/usr/bin/env python3
"""
Production runner for Speed Clicker CTF
Run this for local testing with production Gunicorn settings
"""

import os
import subprocess
import sys

def main():
    print("🚀 Starting Speed Clicker CTF in Production Mode")
    print("=" * 50)
    
    # Set environment variable
    os.environ['ENVIRONMENT'] = 'production'
    
    # Create session directory if it doesn't exist
    session_dir = '/tmp/flask_session'
    os.makedirs(session_dir, exist_ok=True)
    
    print(f"📁 Session directory: {session_dir}")
    print(f"🔧 Environment: {os.environ.get('ENVIRONMENT', 'development')}")
    print(f"🌐 Server will run on: http://localhost:5001")
    print(f"📊 Expected load: ~200 req/second")
    print("-" * 50)
    
    # Run Gunicorn
    try:
        cmd = [
            'gunicorn',
            '--config', 'gunicorn_config.py',
            'app:app'
        ]
        
        print(f"🚀 Executing: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Gunicorn: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Shutting down...")
        sys.exit(0)
    except FileNotFoundError:
        print("❌ Gunicorn not found. Please install requirements:")
        print("   pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main() 