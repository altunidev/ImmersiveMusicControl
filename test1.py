import requests
from pythonosc import dispatcher, osc_server

# Define the Cider API URL
CIDER_API_URL = 'http://localhost:PORT'  # Update with your actual Cider API endpoint

# Function to send HTTP requests to Cider RPC
def send_cider_request(command):
    response = requests.get(f"{CIDER_API_URL}/{command}")
    if response.status_code == 200:
        print(f"Successfully sent command: {command}")
    else:
        print(f"Failed to send command: {command}")

# OSC Handlers (mapping OSC messages to Cider commands)
def play_pause_handler(address, *args):
    send_cider_request('playPause')

def seek_handler(address, *args):
    # Example: OSC message might include a timestamp to seek to
    timestamp = args[0]  # Assuming the first argument is a timestamp
    send_cider_request(f'seekto/{timestamp}')

# Set up dispatcher to handle OSC messages
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/playPause", play_pause_handler)
dispatcher.map("/seek", seek_handler)

# Set up OSC server
osc_server = osc_server.ThreadingOSCUDPServer(('127.0.0.1', 9000), dispatcher)
print("Listening for OSC messages on port 9000...")
osc_server.serve_forever()
