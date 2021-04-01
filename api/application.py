from flask import Flask
DEBUG = True
PORT = 5000
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)