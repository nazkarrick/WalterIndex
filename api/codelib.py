import requests
import json
# from datetime import datetime
"""
API functionality testing,
PYTHON json filtering methods
"""
def jprint(obj):
    # create a formatted string of the PYTHON json object
    # dumps() = takes a PYTHON obj, and converts it to a string
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
response = requests.get('http://api.open-notify.org/iss-now.json')

jprint(response.json())
# for loop to print keys in object
# iss = response.json()
# for keys in iss:
#     print(keys)
# cd = iss['iss_position']
# unxt = iss['timestamp']
# print(cd)
# print(unxt)

# Determine best practice to format unix timestamp.????
# standardTime = []
# time = datetime.fromtimestamp(cd)
# standardTime.append(time)
# print(standardTime)

# jprint(iss['iss_position'])