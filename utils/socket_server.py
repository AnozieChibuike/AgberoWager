import socketio
from games import dice
import eventlet
from models.user import User

sio = socketio.Server()
app = socketio.WSGIApp(sio)

# connections = []

# @sio.event
# def connect(sid, environ):
#     print("connect ", sid)

# @sio.event
# def create_user(data):
    
    

def main():
    eventlet.wsgi.server(eventlet.listen(("", 5000)), app)

if __name__ == "__main__":
    main()