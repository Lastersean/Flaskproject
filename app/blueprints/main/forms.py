from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField,StringField
from wtforms.validators import DataRequired, EqualTo


class PokeForm(FlaskForm):
    poke_request = StringField('Pokemon', validators=[DataRequired()])
    submit_1=SubmitField('I Choose you')