from flask import request, render_template, redirect, url_for, flash
import requests
from app.forms import LoginForm
from app.forms import PokeForm
from app.forms import Signup_form
from app import app




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/user/<username>')
def username(username):
    return  f'Hello today {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


REGISTERED_USERS= {
    'seand@thieves.com' :{
        
        'name': 'Sean Laster',
        'password': 'keepcoding'
    }

}

@app.route('/signup', methods=['GET','POST'])
def signup():
    form=Signup_form()
    if request.method == 'POST' and form.validate_on_submit():
        name=form.first_name.data + ' ' + form.last_name.data
        email=form.email.data.lower()
        password=form.password.data 
        REGISTERED_USERS[email] = {
            'name':name,
            'password':password
        }
        print(REGISTERED_USERS)
        return 'thank you for signing up'
    else:
        return render_template('signup.html', form=form)
        

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if request.method == 'POST' and form.validate_on_submit():
       email = form.email.data.lower()
       password = form.password.data
       if email in REGISTERED_USERS and password == REGISTERED_USERS[email]['password']:
            flash(f"Hi {REGISTERED_USERS[email]['name']} get ready to take the stage!", 'success')
            return redirect(url_for('home'))
       else:
            error = 'Invalid email or password'
            return render_template('login.html', form=form, error=error)
   else:
        print('not validated')
        return render_template('login.html', form=form)
   

@app.route('/pokemon', methods=['GET','POST'])
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