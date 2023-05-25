from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sean'

@app.route('/home')
def home():
    return '<h1>This is the home page</h1>'

@app.route('/user/<username>')
def username(username):
    return  f'Hello today {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       return 'LOGGED IN'
   else:
    return render_template('forms.html')
   d

@app.route('/pokemon', methods=['GET','POST'])
def pokemon():
   if request.method =='POST':
        pokemon = request.form.get('pokemon')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}' 
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_info = []
            
            pokemon_name = response.json()['forms'][0]['name']
            pokemon_dict = {
                'pokemon name': pokemon_name, 
                'Base Experience': response.json()['base_experience'],
                'Ability': response.json()['abilities'][0]['ability']['name'],
                'Sprite' : response.json()['sprites']['back_default']
            }
        return pokemon_dict
   return render_template('pokemon.html')
# add bootstrap table later

     