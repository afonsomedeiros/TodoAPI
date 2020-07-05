from bottle import Bottle
from .routes import create_routes


def create_app():
    app = Bottle()

    create_routes(app)

    return app
