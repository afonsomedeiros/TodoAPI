from bottle import Bottle
from .actions import user_action


def create_user_route(app: Bottle):
    app.get('/users/', callback=user_action.list_user)
    app.post('/users/new/', callback=user_action.create_user)
    app.put('/users/update/', callback=user_action.update_user)

    @app.get('/users/<user_id:int>/')
    def user_view(*args, **kwargs):
        return user_action.view_user(*args, **kwargs)


def create_routes(app: Bottle):

    create_user_route(app)
