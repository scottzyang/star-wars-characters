# imports
from flask import Flask, request, render_template

# initialize app
app = Flask(__name__)

# set API URL
TENOR_URL = 'https://swapi.py4e.com/api/'

# create route for SWAPI results
@app.route('/character_results', methods=['GET'])
def character_search():
  pass
  return render_template('character.html')
