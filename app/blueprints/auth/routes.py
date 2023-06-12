from flask import request, render_template, redirect, url_for, flash
import requests
from app.blueprints.auth.forms import LoginForm
from app.blueprints.auth.forms import Signup_form
from app.models import User
from app import db
from . import auth
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user,current_user,login_required


@auth.route('/signup', methods=['GET','POST'])
def signup():
    form=Signup_form()
    if request.method == 'POST' and form.validate_on_submit():
        user_data = {
            'first_name':form.first_name.data, 
            'last_name': form.last_name.data,
            'email': form.email.data.lower(),
            'password': form.password.data 
            }
       
        new_user = User()
        
        new_user.from_dict(user_data)


        # new_user.first_name = user_data['first_name']
        # new_user.last_name = user_data['last_name']
        # new_user.email = user_data['email']
        # new_user.password =user_data

        db.session.add(new_user)
        db.session.commit()
        
        flash(f'Thank you for signing up {user_data["first_name"]}!', 'success')
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html', form=form)
        

@auth.route('/login', methods=['GET', 'POST'])


def login():
   form = LoginForm()
   if request.method == 'POST' and form.validate_on_submit():
       email = form.email.data.lower()
       password = form.password.data
       queried_user = User.query.filter(User.email == email).first()
       print(queried_user)
       if queried_user and check_password_hash(queried_user.password, password):
            login_user(queried_user)
            flash(f"Hi {queried_user.first_name} get ready to take the stage!", 'success')
            return redirect(url_for('main.home'))
        
       else:
            error = 'Invalid email or password'
            return render_template('login.html', form=form, error=error)
   else:
        print('not validated')
        return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successufully logged out', 'warning')
    return redirect(url_for('auth.login'))