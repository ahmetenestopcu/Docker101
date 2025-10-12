# app.py
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    """This function runs when someone visits the main page."""
    return '<h1>Hello from a Docker Container! 🐳</h1><p>Your Python app is running successfully.</p>'

# Run the app
if __name__ == '__main__':
    # The host '0.0.0.0' is important. It makes the server publicly available
    # inside the container's network, which is required for port mapping to work.
    app.run(host='0.0.0.0', port=5000, debug=True)