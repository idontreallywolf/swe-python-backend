from dotenv import load_dotenv
from app.routes.device import deviceRouter
from app import create_app
from app.database import db
from app.socket import socketio

load_dotenv()

app = create_app()
socketio.init_app(app)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(deviceRouter)


@socketio.on('connect')
def client_connect(auth):
    print("client: ", auth)


@socketio.on('disconnect')
def client_disconnect(reason):
    print('Client disconnected, reason:', reason)


if __name__ == '__main__':
    socketio.run(app)
