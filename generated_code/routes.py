```python
# routes.py
from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    # Logic for user registration
    return jsonify({"message": "User registered successfully."})

@auth.route('/login', methods=['POST'])
def login():
    # Logic for user login
    return jsonify({"message": "User logged in successfully."})
```

```python
# app.py
from flask import Flask
from routes import auth

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
```