
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash



team=db.Table('team',
     db.Column('trainer_id', db.Integer,db.ForeignKey('user.id')),  
     db.Column('pokemon_name', db.String,db.ForeignKey('pokemon.name')),       
              )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True )
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default= datetime.utcnow)
    pokemon= db.relationship('Pokemon',secondary=team, backref='trainer', lazy='dynamic')
    post= db.relationship('Post',backref='author', lazy='dynamic')

    def add_team(self, poke):
        self.pokemon.append(poke)
        db.session.commit()

    def release(self,poke):
        self.pokemon.remove(poke)
        db.session.commit()

    



    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)   

    def from_dict(self, user_data):
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email']
        self.password = self.hash_password(user_data['password'])

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Pokemon(db.Model):
    name= db.Column(db.String, primary_key=True)
    base_experience= db.Column(db.Integer,nullable=False)
    ability=  db.Column(db.String,nullable=False)
    sprite= db.Column(db.String,nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def from_dict(self, pokedata):
        self.name= pokedata['pokemon name']
        self.base_experience= pokedata['Base Experience']
        self.ability= pokedata['Ability']
        self.sprite= pokedata['Sprite']

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    img_url=db.Column(db.String)
    title=db.Column(db.String)
    caption=db.Column(db.String)
    created_on=db.Column(db.DateTime, default=datetime.utcnow())
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

    def from_dict(self, post_data):
        self.img_url= post_data['img_url']
        self.title=post_data['title']
        self.caption=post_data['caption']
        self.user_id=post_data['user_id']