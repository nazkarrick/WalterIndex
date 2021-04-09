# FUNCTIONAL TASKS: 
"""
FOUND UI ISSUES:
1. Data Visualization Tools are not properly rendering. 
"""
from flask import Flask, render_template
from flask_wtf import Form
from wtforms.fields.html5 import DateField
import requests
import json

DEBUG = True
PORT = 5000
app = Flask(__name__)
app.secret_key = 'SHH'

#####=== GLOBAL ===#####
class SearchForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')
#########======#########

#######====== INDEX ======#######
@app.route('/', methods=['POST', 'GET'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        date_query = form.dt.data.strftime('%Y-%m-%d')
        api_nasa = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=WWWXENdMExrIHV2WTMh3baouTEuBpkcmrQqRZtb8&date={date_query}')
        res = json.loads(api_nasa.content)
        # to view JSON object comment out line 34 and replace with < return res  >
        return render_template('return_date.html', res=res)
    return render_template('main.html', form=form)
########===========##################

#########=== Navigation Bar ===#########
@app.route('/apod', methods=['GET'])
def get_apod():
    apod_query = requests.get('https://api.nasa.gov/planetary/apod?api_key=WWWXENdMExrIHV2WTMh3baouTEuBpkcmrQqRZtb8')
    res = json.loads(apod_query.content)
    return render_template('apod.html', res=res)

@app.route('/iss', methods=['GET'])
def get_iss():
    issLoc = requests.get('http://api.open-notify.org/iss-now.json')
    issRes = json.loads(issLoc.content)
    return render_template('iss.html', issRes=issRes )
###########===============###############

# PYTHON: FLASK/JINJA2: NASA OPEN API, ISS OPEN API
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)