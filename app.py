from flask import Flask, render_template
from flask_socketio import Socketio

app = Flask(__name__)
socketIO = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketIO.on('mensaje')
def handle_mensaje():
    return "algo"
    socketIO.emit('mensaje', msg)

if __name__ == "__main__":
    socketIO.run(app, debug = True)
