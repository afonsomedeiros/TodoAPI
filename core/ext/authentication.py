from bottle import Bottle
from .JwtPlugin import JWTPlugin
from settings import JWT_SECRET
from peewee import DoesNotExist

from core.models import Users
from core.serializers import UserSchema


def install_auth(app: Bottle):
    """Realiza instalacao do plugin de autenticacao JWT.

    Args:
        app (Bottle): instancia de uma aplicação Bottle onde
        sera instalado o Plugin.
    """
    jwt = JWTPlugin(JWT_SECRET, Users, refresh=True)
    app.install(jwt)