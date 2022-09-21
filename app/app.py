from flask import Flask
import socket

app = Flask(__name__)

# Route for the default page
@app.route("/")
def home():
    # Display message
    return f'<center><h3>Welcome to GFG <h1>{socket.gethostname()}</h1></h3></center>'

if __name__ == '__main__':
    app.run('0.0.0.0')