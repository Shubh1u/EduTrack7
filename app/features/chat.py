from flask import Blueprint, render_template, session
from flask_socketio import emit, join_room
from app import socketio
from app.utils import login_required

chat_bp = Blueprint('chat', __name__, template_folder='../templates')

@chat_bp.route('/chat')
@login_required
def chat():
    return render_template('chat.html', username=session.get('username', 'Guest'))

@socketio.on('join')
def handle_join(data):
    room = 'global'
    join_room(room)
    emit('message', {'user': 'System', 'msg': f"{data.get('user', 'User')} joined the chat"}, room=room)

@socketio.on('send_message')
def handle_message(data):
    room = 'global'
    user = data.get('user', 'User')
    msg = data.get('msg', '')
    if msg.strip():
        emit('message', {'user': user, 'msg': msg}, room=room)
