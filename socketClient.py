import socketio
from models.user import User
# Create a Socket.IO client
sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")
    sio.emit('my_message', {'message': 'Hello server!'}) # Send a message to the server

def create_game_callback(data):
    print(f'Invite code: {data}\nShare it with friend')

def create_game(host,stake):
    sio.emit('create_game',{'host':host,'stake':stake},callback=create_game_callback)

@sio.event
def join_game_callback(data):
    print(data)
    
def join_game(id,party):
    sio.emit('join_game',{'id':id,'party':party})

@sio.event
def disconnect():
    print("I'm disconnected!")

if __name__ == '__main__':
    import time
    
    join = input('join/create?')
    sio.connect('http://localhost:5000')
    if join.lower() == 'create':
        create_game(1,200)
    else:
        join_game(input('id'),2)
    time.sleep(100)    
