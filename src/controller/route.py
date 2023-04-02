from flask import Blueprint

from src.emailServer import SMTP

routes = Blueprint("routes",__name__,url_prefix="/app/v1/")

healthCheck = Blueprint("healthCheck",__name__,url_prefix="/")

@healthCheck.get('liveness')
def test():
    response = Response(json.dumps({'liveness': True}),status=200,content_type="application/json")
    return response

@routes.post('email')
def sendEmail():
    return SMTP()

