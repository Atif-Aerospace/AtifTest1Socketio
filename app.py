from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('create_data')
def handle_create_data(json):
    print('received json: ' + str(json))
    emit('create_data', json, broadcast=True)


@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, port=80)