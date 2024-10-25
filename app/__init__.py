from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.routes import main_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Initialize the database with the app
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(main_blueprint)
    
    return app
