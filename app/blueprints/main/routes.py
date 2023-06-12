from flask import request, render_template
import requests
from app.blueprints.main.forms import PokeForm
from . import main
from flask_login import login_required

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/user/<username>')
def username(username):
    return  f'Hello today {username}'

@main.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@main.route('/pokemon', methods=['GET','POST'])
@login_required
def pokemon():
   form = PokeForm()
   if request.method =='POST':
        pokemon = form.poke_request.data.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}' 
        response = requests.get(url)
        if response.status_code == 200:
            
            pokemon_name = response.json()['forms'][0]['name']
            pokemon_dict = {
                'pokemon name': pokemon_name, 
                'Base Experience': response.json()['base_experience'],
                'Ability': response.json()['abilities'][0]['ability']['name'],
                'Sprite' : response.json()['sprites']['back_default'],
                'Pokemon Index': response.json()['id']
            }
            
        return render_template('pokemon.html', pokemon_dict= pokemon_dict, form=form)
   return render_template('pokemon.html', form=form)
# add bootstrap table later


