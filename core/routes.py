from bottle import Bottle
from .actions import user_action, task_action
from core.ext import auth_required


def create_user_route(app: Bottle):
    app.get('/users/', callback=user_action.list_user)
    app.post('/users/new/', callback=user_action.create_user)
    app.put('/users/update/', callback=user_action.update_user)

    @app.get('/users/<user_id:int>/')
    def user_view(*args, **kwargs):
        return user_action.view_user(*args, **kwargs)


def create_task_route(app: Bottle):
    app.get('/tasks/', callback=task_action.list_task)
    app.post('/tasks/new/', callback=task_action.create_task)
    app.put('/tasks/update/', callback=task_action.update_task)

    @app.get('/tasks/<task_id:int>/')
    def task_view(*args, **kwargs):
        return task_action.view_task(*args, **kwargs)


def create_routes(app: Bottle):

    create_user_route(app)
    create_task_route(app)
