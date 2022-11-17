# imports
from flask import Flask, request, render_template
import json
import requests

# initialize app
app = Flask(__name__)

# set API URL
SWAPI_URL = 'https://swapi.py4e.com/api/'

# create route for SWAPI results
@app.route('/', methods=['GET'])
def character_search():
  character_id = request.args.get('character-id')
  if not character_id:
    character_id = '1'

  response = requests.get(SWAPI_URL + "people/" + character_id)

  character_info = response.json()

  context = {
    'character_info': character_info
  }

  return render_template('character.html', **context)


if __name__ == '__main__':
    app.run(debug=True)