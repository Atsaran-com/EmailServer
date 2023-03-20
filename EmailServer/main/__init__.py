from flask import Flask
from dotenv import load_dotenv

from main.controller.route import routes

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app

app = create_app()

