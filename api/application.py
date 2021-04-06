# FUNCTIONAL TASKS: 
# [] FIX GLOBAL API 
# [] Add borders within Card  /templates/apod  
# [] Add UI styling to Cards
# [] Visual for ISS Coordinates
# [] Adjust spacing in Nav Bar

from flask import Flask, render_template
from flask_wtf import Form
from wtforms.fields.html5 import DateField
import requests
import json

DEBUG = True
PORT = 5000
app = Flask(__name__)
app.secret_key = 'SHH'

###=== GLOBAL VARIABLES ===###
api_nasa = requests.get('https://api.nasa.gov/planetary/apod?api_key=WWWXENdMExrIHV2WTMh3baouTEuBpkcmrQqRZtb8')
issLoc = requests.get('http://api.open-notify.org/iss-now.json')
class SearchForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')
#########======#########

##== INDEX ==##
@app.route('/', methods=['POST', 'GET'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        return form.dt.data.strftime('%Y-%m-%d')
    return render_template('main.html', form=form)
##===========##

#########=== Navigation Bar ===#########
@app.route('/apod', methods=['GET'])
def get_apod():
    res = json.loads(api_nasa.content)
    return render_template('apod.html', res=res)

@app.route('/iss', methods=['GET'])
def get_iss():
    issRes = json.loads(issLoc.content)
    return render_template('iss.html', issRes=issRes )
###########===============###############

# PYTHON: FLASK/JINJA2: NASA OPEN API, ISS OPEN API
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)