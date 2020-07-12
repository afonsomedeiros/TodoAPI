from bottle import Bottle
from .routes import create_routes
from .ext import install_auth


def create_app():
    app = Bottle()
    
    create_routes(app)
    install_auth(app)

    return app
