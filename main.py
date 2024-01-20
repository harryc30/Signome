from types import SimpleNamespace
from flask import Flask, render_template, request, json, jsonify, Response
import cv2

curList = []
pastList = []

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contactus")
def contact():
    return render_template("contact.html")

if not camera.isOpened():
    raise IOError("Cannot access the camera")

def gen_frames():
    while True:
        bleh,frame = camera.read()
        ret,buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

prevImage = None
transcription = "hello hack the north"
def take_image():
    global prevImage
    bleh,frame = camera.read()
    resizeValue = (28,28)
    prevImage = cv2.resize(frame,resizeValue, interpolation = cv2.INTER_AREA)
    return render_template("home.html")

@app.route("/taking_image")
def taking_image():
    return take_image()

@app.route('/postmethod', methods=['GET', 'POST'])
def get_javascript_data():
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200
    # GET request
    else:
        message = 'greeting Hello from Flask!'
        return jsonify(message)  # serialize and use JSON headers

if __name__ == "__main__":
    app.run(debug=True)
