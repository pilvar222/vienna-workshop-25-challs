#!/usr/bin/env python3
"""
Basic Speed Clicker Solution using requests.Session()

This is the simplest possible solution that demonstrates:
1. Using requests.Session() to maintain session cookies
2. Sending POST requests to start the game and click rapidly
3. Parsing JSON responses to track progress
"""

import requests
import time

def main():
    # Create a session object to maintain cookies across requests
    session = requests.Session()
    
    # Base URL of the Flask application
    base_url = "http://34.176.207.5:9005"
    
    print("🎮 Basic Speed Clicker Solution")
    print(f"🌐 Connecting to: {base_url}")
    
    try:
        # Step 1: Start a new game
        print("\n1. Starting new game...")
        start_response = session.post(f"{base_url}/start")
        start_data = start_response.json()
        print(f"   ✅ Game started: {start_data['message']}")
        
        # Step 2: Send clicks as fast as possible
        print("\n2. Sending rapid clicks...")
        clicks = 0
        start_time = time.time()
        
        while True:
            # Send a click request using the session
            response = session.post(f"{base_url}/click")
            data = response.json()
            clicks += 1
            
            # Print progress occasionally
            if clicks % 5 == 0:
                print(f"   📊 Progress: {data['score']}/100 in {data['elapsed_time']:.3f}s")
            
            # Check if game is over
            if data.get('game_over', False):
                end_time = time.time()
                execution_time = end_time - start_time
                
                print(f"\n3. Game completed!")
                print(f"   📈 Total clicks sent: {clicks}")
                print(f"   ⏱️  Execution time: {execution_time:.3f} seconds")
                print(f"   🎯 Final score: {data['score']}/100")
                print(f"   🕐 Game time: {data['elapsed_time']:.3f} seconds")
                
                if data.get('won', False):
                    print(f"   🎉 SUCCESS! You won!")
                    print(f"   🚩 Flag: {data.get('flag', 'Not found')}")
                    print(f"   💬 Message: {data['message']}")
                else:
                    print(f"   ❌ Game over: {data['message']}")
                
                break
                
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to the Flask application")
        print("   Make sure the server is running with: python app.py")
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main() 