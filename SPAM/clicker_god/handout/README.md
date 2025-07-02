# Speed Clicker Challenge 🚀 (Production Ready)

A fast-paced clicking game where you need to click a button 100 times in under 3 seconds to win the flag! This version is optimized for production deployment and can handle ~200 req/second from tens of concurrent users.

## Features

- **Session-based scoring**: Each click sends a POST request to the backend with session tracking
- **Time limit**: 3 seconds to complete the challenge
- **Real-time updates**: Live score and timer display
- **Modern UI**: Beautiful, responsive design with animations
- **Flag reward**: Win the flag `vienna{fake_flag}` by completing the challenge
- **Keyboard support**: Use spacebar to click faster
- **Production ready**: Optimized with Gunicorn + gevent for high concurrency

## Game Rules

1. Click "Start Game" to begin
2. Click the red button (or press spacebar) as fast as possible
3. Reach 100 clicks within 3 seconds to win
4. If time runs out, you lose and must restart

## 🚀 Running in Production

### Method 1: Docker (Recommended)

```bash
# Build the Docker image
docker build -t speed-clicker .

# Run the container
docker run -p 5001:5001 speed-clicker
```

### Method 2: Local Production Server

```bash
# Install dependencies
pip install -r requirements.txt

# Run with production Gunicorn server
python run_production.py
```

### Method 3: Development Mode

```bash
# Install dependencies
pip install -r requirements.txt

# Run the basic Flask dev server (not recommended for load)
python app.py
```

Visit `http://localhost:5001` in your browser to play the game!

## 🔧 Production Configuration

The production setup uses:

- **Gunicorn WSGI server** with gevent workers for async I/O
- **Multiple worker processes** (auto-scaled based on CPU cores)
- **Worker recycling** to prevent memory leaks
- **Optimized timeouts** and connection handling
- **Shared session storage** in `/tmp/flask_session`
- **Non-root container** for security

### Performance Characteristics

- **Capacity**: ~200 requests/second
- **Concurrent users**: Tens of simultaneous players
- **Session storage**: Filesystem-based (filesystem sessions work across Gunicorn workers)
- **Memory usage**: Low (~50MB base + ~10MB per worker)
- **CPU usage**: Scales with worker count

## 🧪 Load Testing

Test the server's performance:

```bash
# Install test dependencies
pip install requests

# Run load test (20 users for 30 seconds)
python load_test.py

# Custom load test
python load_test.py --users 30 --duration 60 --url http://localhost:5001
```

Expected results:
- **>200 req/sec**: Excellent performance ✅
- **150-200 req/sec**: Good performance ✅
- **100-150 req/sec**: Acceptable ⚠️
- **<100 req/sec**: Needs improvement ❌

## 🎯 Solution Scripts

Use the automated solution to beat the challenge:

```bash
# Install solution dependencies
pip install requests

# Run the solution script
python solution.py
```

## Technical Details

### Backend Architecture
- **Framework**: Flask with Flask-Session
- **WSGI Server**: Gunicorn with gevent workers
- **Session Storage**: Filesystem-based (shared across workers)
- **Security**: Random secret key generation, session signing
- **Process Management**: Multiple workers with request recycling

### Frontend
- **Technology**: Modern HTML/CSS/JavaScript
- **Communication**: Real-time AJAX updates
- **UX**: Responsive design with animations
- **Performance**: Optimized for rapid clicking

### Docker Configuration
- **Base Image**: Python 3.11-slim
- **Security**: Non-root user execution
- **Optimization**: Multi-stage build, layer caching
- **Persistence**: Session data in `/tmp/flask_session`

## API Endpoints

- `GET /` - Game interface
- `POST /start` - Initialize new game session
- `POST /click` - Process click and update score
- `GET /status` - Get current game status

## 🔒 Security Considerations

- Sessions use cryptographic signing
- Rate limiting handled by session validation
- Non-root container execution
- Input validation on all endpoints
- Secure session storage

## 🏆 Performance Optimization

The production setup includes:

1. **Gunicorn Configuration**:
   - Worker auto-scaling based on CPU cores
   - Gevent async workers for I/O concurrency
   - Request recycling to prevent memory leaks

2. **Session Management**:
   - Filesystem storage shared across workers
   - Session cleanup and expiration
   - Cryptographic session signing

3. **Resource Management**:
   - Worker memory limits
   - Connection pooling
   - Optimized timeouts

## Challenge

This is quite difficult! 100 clicks in 3 seconds requires averaging over 33 clicks per second. The production server is optimized to handle this load from multiple concurrent users. Good luck! 🎯

## Monitoring

Monitor the application with:

```bash
# Check Gunicorn workers
ps aux | grep gunicorn

# Monitor session files
ls -la /tmp/flask_session/

# Watch logs
docker logs -f <container_id>
``` 