```python
# Importing required libraries
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Function to facilitate social learning and collaboration
def facilitateSocialLearning():
    @socketio.on('join')
    def on_join(data):
        username = data['username']
        room = data['room']
        join_room(room)
        send({"message": username + ' has entered the room.'}, room=room)

    @socketio.on('leave')
    def on_leave(data):
        username = data['username']
        room = data['room']
        leave_room(room)
        send({"message": username + ' has left the room.'}, room=room)

    @socketio.on('message')
    def message(data):
        send({"message": data['message']}, room=data['room'])

    @socketio.on('connect')
    def test_connect():
        print('Client connected')

    @socketio.on('disconnect')
    def test_disconnect():
        print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
```
This code creates a Flask application with SocketIO to facilitate real-time communication for social learning. Users can join and leave rooms (study groups), and send messages within these rooms. The 'connect' and 'disconnect' events are logged for monitoring purposes.