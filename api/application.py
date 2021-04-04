from flask import Flask, render_template
import requests
import json

DEBUG = True
PORT = 5000
app = Flask(__name__)



#########=== Navigation Bar ===#########

@app.route('/', methods=['GET'])
def index():
    api_nasa = requests.get('https://api.nasa.gov/planetary/apod?api_key=WWWXENdMExrIHV2WTMh3baouTEuBpkcmrQqRZtb8')
    res = json.loads(api_nasa.content)
    return render_template('apod.html', res=res)

@app.route('/iss', methods=['GET'])
def get_iss():
    issLoc = requests.get('http://api.open-notify.org/iss-now.json')
    issRes = json.loads(issLoc.content)
    return render_template('iss.html', issRes=issRes )

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)