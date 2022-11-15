# imports
from flask import Flask, request, render_template
import json
import requests

# initialize app
app = Flask(__name__)

# set API URL
SWAPI_URL = 'https://swapi.py4e.com/api/people/1'

# create route for SWAPI results
@app.route('/', methods=['GET'])
def character_search():
  # character_id = request.args.get('character-id')

  response = requests.get(
    SWAPI_URL)

  character_info = response.json()

  context = {
    'character_info': character_info
  }

  return render_template('character.html', **context)


if __name__ == '__main__':
    app.run(debug=True)