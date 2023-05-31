from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField,StringField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    email = EmailField('Email:',  validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')

class PokeForm(FlaskForm):
    poke_request = StringField('Pokemon', validators=[DataRequired()])
    submit_1=SubmitField('I Choose you')

class Signup_form(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password')])
    submit_2= SubmitField('Sign Up')