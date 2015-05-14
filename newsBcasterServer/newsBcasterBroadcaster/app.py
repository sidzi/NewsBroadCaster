import os

from flask import Flask, render_template, Response

from newsBcasterServer.newsBcasterBroadcaster.camera import Camera


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(__name__, template_folder=tmpl_dir, static_folder=static_dir)

@app.route("/")
def index_page():
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
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)