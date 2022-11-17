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
  # git input from form
  character_id = request.args.get('character-id')
  # if input is not provided, default to 1
  if not character_id:
    character_id = '1'

  # get character info response using the character ID above and parse to python
  response = requests.get(SWAPI_URL + "people/" + character_id)
  character_info = response.json()
  
  # get homeworld response using character above, and parse to python
  homeworld_response = requests.get(character_info['homeworld'])
  current_homeworld = homeworld_response.json()

  # list comprehension
  # for each film in the character_info.films grab response for each film API URL and parse it to python, and acquire the name
  # once acquired, add it to the list
  films = [requests.get(film).json()['title'] for film in character_info['films']]

  context = {
    'character_info': character_info,
    'films': films,
    'homeworld': current_homeworld
  }

  return render_template('character.html', **context)


if __name__ == '__main__':
    app.run(debug=True)