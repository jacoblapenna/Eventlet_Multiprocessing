
# import eventlet
# eventlet.monkey_patch()

from gevent import monkey
monkey.patch_all()

from random import randrange
import time

from redis import Redis

from flask import Flask, render_template, request
from flask_socketio import SocketIO
from celery import Celery
from celery.contrib import rdb


def message_queue(db):
    return f"redis://localhost:6379/{db}"

app = Flask(__name__)
socketio = SocketIO(app, message_queue=message_queue(0), async_mode="gevent")

# cel = Celery("backend", broker=message_queue(0), backend=message_queue(0))

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on("start_data_stream")
def start_data_stream():
    socketio.emit("new_data", {"value" :  666})
    # stream_data.delay(request.sid)

# @cel.task()
# def stream_data(sid):

#     # data_socketio = SocketIO(message_queue=message_queue(0))
#     i = 1

#     while i <= 100:
#         value = randrange(0, 10000, 1) / 100
#         # data_socketio.emit("new_data", {"value" :  value})
#         i += 1
#         time.sleep(0.01)
    
#     # rdb.set_trace()

#     return i, value


if __name__ == "__main__":

    r = Redis()
    r.flushall()

    if r.ping():
        pass
    else:
        raise Exception("You need redis: https://redis.io/docs/getting-started/installation/. Check that redis-server.service is running!")

    ip = "192.168.1.8" # insert LAN address here
    port = 8080

    socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)
