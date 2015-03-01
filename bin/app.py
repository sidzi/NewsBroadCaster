#!/usr/bin/env python
from flask import Flask, render_template, Response

# emulated camera
from newsbcasttemplater.camera import Camera

import Tkinter as tk

import socket

import time

serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 4500
serversocket.bind((host,port))
serversocket.listen(5)

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        b = tk.Button(self,text="Ok", command=app.run)
        b.pack()

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    clientsocket,addr = serversocket.accept()
    print ("Connection from ABCD %s" % str(addr))
    clientsocket.close()
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    appgui = Application()
    appgui.master.title('Sample application')
    appgui.mainloop()
