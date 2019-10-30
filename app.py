from flask import Flask
from flask_socketio import SocketIO
from logging import Formatter, FileHandler
import logging

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('connect', namespace='socketio')
def connect():
    app.logger.info('connection')


@socketio.on('name_event', namespace='socketio')
def name(json):
    app.logger.info('first name: ' + json['first_name'] + ', last name: ' + json['last_name'])


@app.route('/name/<name>')
def hello_world(name):
    app.logger.info("My name is " + name)
    return 'My name is ' + name


if __name__ == '__main__':
    file_handler = FileHandler('/flasksocketiosample/output.log')
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    socketio.run(app, host='0.0.0.0', port=12380, debug=True)
