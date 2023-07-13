from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate






login_manager = LoginManager()
db = SQLAlchemy()



migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # registering packages
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # login settings
    login_manager.login_view='auth.login'
    login_manager.login_message = 'You must be logged in to visit this page'
    login_manager.login_message_category= 'warning'
    

    # importing blueprints
    from app.blueprints.main import main
    from app.blueprints.auth import auth
    from app.blueprints.post import post

    # registering blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(post)

    return app

# from app import models
