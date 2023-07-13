from flask import request, render_template, flash,redirect,url_for
import requests
from . import main
from flask_login import login_required, current_user
from app.models import User






@main.route('/')
@main.route('/home')
def home():
    
    
    return render_template('home.html' )

@main.route('/user/<username>')
def username(username):
    return  f'Hello today {username}'

@main.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'




@main.route('/products',  methods=['GET', 'POST'])
def product():
    
    return render_template('product.html')


