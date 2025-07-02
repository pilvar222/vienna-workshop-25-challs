from flask import Flask, session, request, jsonify, render_template
from flask_session import Session
import time
import secrets
import os

app = Flask(__name__)

# Generate random secret key
app.config['SECRET_KEY'] = secrets.token_hex(32)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    """Initialize a new game session"""
    session['score'] = 0
    session['start_time'] = time.time()
    session['game_over'] = False
    session['won'] = False
    
    return jsonify({
        'score': session['score'],
        'start_time': session['start_time'],
        'message': 'Game started! Click as fast as you can!'
    })

@app.route('/click', methods=['POST'])
def click():
    """Handle click events and update score"""
    if 'start_time' not in session:
        return jsonify({'error': 'Game not started'}), 400
    
    if session.get('game_over', False):
        return jsonify({'error': 'Game already over'}), 400
    
    current_time = time.time()
    elapsed_time = current_time - session['start_time']
    
    # Check if time limit exceeded
    if elapsed_time > 3.0:
        session['game_over'] = True
        return jsonify({
            'score': session['score'],
            'elapsed_time': elapsed_time,
            'game_over': True,
            'won': False,
            'message': 'Time\'s up! You lost!'
        })
    
    # Increment score
    session['score'] = session.get('score', 0) + 1
    
    # Check win condition (100 clicks in less than 3 seconds)
    if session['score'] >= 100:
        session['game_over'] = True
        session['won'] = True
        return jsonify({
            'score': session['score'],
            'elapsed_time': elapsed_time,
            'game_over': True,
            'won': True,
            'flag': 'vienna{fake_flag}',
            'message': f'Congratulations! You won with {session["score"]} clicks in {elapsed_time:.2f} seconds!'
        })
    
    return jsonify({
        'score': session['score'],
        'elapsed_time': elapsed_time,
        'game_over': False,
        'won': False,
        'message': f'Score: {session["score"]}/100'
    })

@app.route('/status', methods=['GET'])
def status():
    """Get current game status"""
    if 'start_time' not in session:
        return jsonify({'game_started': False})
    
    current_time = time.time()
    elapsed_time = current_time - session['start_time']
    
    return jsonify({
        'game_started': True,
        'score': session.get('score', 0),
        'elapsed_time': elapsed_time,
        'game_over': session.get('game_over', False),
        'won': session.get('won', False)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) 