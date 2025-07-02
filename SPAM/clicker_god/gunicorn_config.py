# Gunicorn configuration for Speed Clicker CTF
# Optimized for ~200 req/second with tens of concurrent users

import multiprocessing
import os

# Server socket
bind = "0.0.0.0:5001"
backlog = 2048

# Worker processes
workers = min(multiprocessing.cpu_count() * 2 + 1, 8)  # Cap at 8 workers
worker_class = "gevent"  # Use gevent for better I/O concurrency
worker_connections = 1000
max_requests = 10000
max_requests_jitter = 1000

# Timeouts
timeout = 30
keepalive = 2

# Logging
loglevel = "info"
accesslog = "-"
errorlog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "speed_clicker_ctf"

# Preload app for better performance
preload_app = True

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Performance tuning
worker_tmp_dir = "/dev/shm" if os.path.exists("/dev/shm") else None

def when_ready(server):
    server.log.info("Speed Clicker CTF server is ready. Expecting ~200 req/sec load.")

def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

def on_exit(server):
    server.log.info("Speed Clicker CTF server is shutting down.")

# Environment-specific settings
if os.environ.get('ENVIRONMENT') == 'production':
    # Production settings
    workers = multiprocessing.cpu_count() * 2 + 1
    worker_connections = 2000
    preload_app = True
else:
    # Development settings
    workers = 2
    reload = True 