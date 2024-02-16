import socketio
import random
from games.dice import Dice
from models.user import User

# Create a Socket.IO server
sio = socketio.Server()

# Create a Flask application
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print("connect ", sid)

u1 = User(username='Queens', age=20, country="Nigeria")
u2 = User(username='Queensol', age=20, country="Nigeria")
u1.id = 1
u2.id = 2

@sio.event
def join_game(sid,data):
    game = list(filter(lambda x: x.id == data['id'],Dice.games))
    if not game:
        sio.emit('join_game_callback','Game does not exists with such id') 
    if game[0].played:
        sio.emit('join_game_callback','Game already played')
    game[0].user2 = User.get(id=data['party'])[0]
    sio.emit('join_game_callback','Game created ready to play')

@sio.event
def disconnect(sid):
    print("disconnect ", sid)

@sio.event
def create_game(sid,data):
    game = Dice(User.get(id=data['host'])[0],User.get(id=data['host'])[0],data['stake'])
    return game.id

if __name__ == "__main__":
    import eventlet
    
    eventlet.wsgi.server(eventlet.listen(("", 5000)), app)
