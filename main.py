# imports
from flask import Flask, request, render_template
import json
import requests
import os
from dotenv import load_dotenv

# initialize app
app = Flask(__name__)

# search macOS for api key
API_KEY = os.getenv('API_KEY')

# set API URL
SWAPI_URL = 'https://swapi.py4e.com/api/'
TENOR_URL = 'https://tenor.googleapis.com/v2/search?'

# create route for SWAPI results
@app.route('/', methods=['GET'])
def character_search():
  # git input from form
  character_id = request.args.get('character-id')
  # if input is not provided, default to 1
  if not character_id:
    character_id = '0'

  # get character info response using the character ID above and parse to python
  response = requests.get(SWAPI_URL + "people/" + character_id)
  character_info = response.json()
  
  # get homeworld response using character above, and parse to python
  try:
    homeworld_response = requests.get(character_info['homeworld'])
    current_homeworld = homeworld_response.json()
  except KeyError:
    print(f'KeyError: Setting current_homeworld to N/A')
    current_homeworld = 'N/A'

  # list comprehension
  # for each film in the character_info.films grab response for each film API URL and parse it to python, and acquire the name
  # once acquired, add it to the list
  try:
    films = [requests.get(film).json()['title'] for film in character_info['films']]
  except KeyError:
    print('KeyError: Setting films to N/A')
    films = ['N/A']

  try:
    character_name = character_info['name']
  except KeyError:
    print('KeyError: Setting character_name to Star Wars')
    character_name = 'Star Wars'

  # get gif from tenor url
  tenor_request = requests.get(
    TENOR_URL, 
  {
    'q': character_name,
    'key': API_KEY,
    'limit': 1,
  })

  gifs = json.loads(tenor_request.content).get('results')
  

  context = {
    'character_info': character_info,
    'films': films,
    'homeworld': current_homeworld,
    'gifs': gifs
  }

  return render_template('character.html', **context)


if __name__ == '__main__':
    app.run(debug=True)