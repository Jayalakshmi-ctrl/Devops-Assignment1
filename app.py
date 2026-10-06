from flask import Flask
from routes import api

def create_app():
    app = Flask(__name__)
    
    # Mount modular v1 blueprints
    app.register_blueprint(api)
    
    return app

app = create_app()

if __name__ == '__main__':
    # Binds server port for local loop testing
    app.run(host='0.0.0.0', port=5000, debug=True)
