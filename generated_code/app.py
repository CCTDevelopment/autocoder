```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import main_blueprint
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object(Config)
    
    # Initialize the database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(main_blueprint)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
```