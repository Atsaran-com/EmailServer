from flask import Flask
from dotenv import load_dotenv
from gevent.pywsgi import WSGIServer

from src.controller.route import routes, healthCheck

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.register_blueprint(healthCheck)
    return app
# setting flask to run on production mode
def production():
    http_server = WSGIServer((os.environ.get("FLASK_RUN_HOST"), int(os.environ['FLASK_RUN_PORT'])), app)
    http_server.serve_forever()
    
if os.environ.get("FLASK_ENV") == 'production':
    production()
    
app = create_app()

