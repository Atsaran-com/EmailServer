from flask import Blueprint

from main.emailServer import SMTP

routes = Blueprint("routes",__name__,url_prefix="/")

@routes.get('test')
def test():
    return "hai"

@routes.post('email')
def sendEmail():
    return SMTP()

