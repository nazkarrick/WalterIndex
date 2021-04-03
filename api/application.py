from flask import Flask, render_template
import requests
import json

DEBUG = True
PORT = 5000
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    api_nasa = requests.get('https://api.nasa.gov/planetary/apod?api_key=WWWXENdMExrIHV2WTMh3baouTEuBpkcmrQqRZtb8')
    res = json.loads(api_nasa.content)
    return render_template('index.html', res=res)

@app.route('/apod')
def get_apod():
    return {"apod": "apod data"}

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)