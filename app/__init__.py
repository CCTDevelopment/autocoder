from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config  # Relative import
from .routes import main_blueprint  # Relative import

# Initialize the SQLAlchemy database instance
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
