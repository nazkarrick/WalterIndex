# FUNCTIONAL TASKS: 
# [] Mailing List API for Database
# [] Visual for ISS Coordinates
# [] Date Validator to prevent searching further than 06-16-1995 & current date

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
        # to view JSON object comment out line 34 and replace with< return res  >
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

########===== MAIL LIST API =====##########
from mailjet_rest import Client
import os
api_key = '05a8c6a9bd9006ba756f22db838ae3fc'
api_secret = '1c1559462c80b9c203c1b7c10c3eee76'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
    'Messages': [
            {
            "From": {
                "Email": "designed.x.horo@gmail.com",
                "Name": "Robert"
            },
            "To": [
                {
                "Email": "designed.x.horo@gmail.com",
                "Name": "Robert"
                }
            ],
            "Subject": "Greetings from Mailjet.",
            "TextPart": "My first Mailjet email",
            "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
            "CustomID": "AppGettingStartedTest"
            }
    ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())


# PYTHON: FLASK/JINJA2: NASA OPEN API, ISS OPEN API
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)