from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Store active rooms and users
rooms = {}
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/room/<room_id>')
def room(room_id):
    return render_template('room.html', room_id=room_id)

@socketio.on('connect')
def on_connect():
    print(f'User {request.sid} connected')

@socketio.on('disconnect')
def on_disconnect():
    print(f'User {request.sid} disconnected')
    # Clean up user from rooms
    user_id = request.sid
    if user_id in users:
        room_id = users[user_id].get('room')
        if room_id and room_id in rooms:
            rooms[room_id].discard(user_id)
            if not rooms[room_id]:
                del rooms[room_id]
            else:
                emit('user_left', {'user_id': user_id}, room=room_id)
        del users[user_id]

@socketio.on('join_room')
def on_join_room(data):
    room_id = data['room_id']
    user_id = request.sid
    username = data.get('username', f'User_{user_id[:8]}')
    
    join_room(room_id)
    
    # Initialize room if it doesn't exist
    if room_id not in rooms:
        rooms[room_id] = set()
    
    # Add user to room
    rooms[room_id].add(user_id)
    users[user_id] = {'room': room_id, 'username': username}
    
    # Notify others in the room
    emit('user_joined', {
        'user_id': user_id,
        'username': username,
        'room_users': list(rooms[room_id])
    }, room=room_id)
    
    print(f'User {username} ({user_id}) joined room {room_id}')

@socketio.on('leave_room')
def on_leave_room(data):
    room_id = data['room_id']
    user_id = request.sid
    
    leave_room(room_id)
    
    if room_id in rooms:
        rooms[room_id].discard(user_id)
        if not rooms[room_id]:
            del rooms[room_id]
        else:
            emit('user_left', {'user_id': user_id}, room=room_id)
    
    if user_id in users:
        del users[user_id]

# WebRTC signaling events
@socketio.on('offer')
def handle_offer(data):
    data['sender'] = request.sid
    emit('offer', data, room=data['target'])

@socketio.on('answer')
def handle_answer(data):
    data['sender'] = request.sid
    emit('answer', data, room=data['target'])

@socketio.on('ice_candidate')
def handle_ice_candidate(data):
    data['sender'] = request.sid
    emit('ice_candidate', data, room=data['target'])

@socketio.on('ready')
def handle_ready(data):
    room_id = data['room_id']
    emit('ready', {'user_id': request.sid}, room=room_id, include_self=False)

@socketio.on('ready')
def handle_ready(data):
    room_id = data['room_id']
    emit('ready', {'user_id': request.sid}, room=room_id, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
