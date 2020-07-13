from bottle import Bottle
from .actions import user_action, task_action
from jwt_bottle import auth_required


def create_user_route(app: Bottle):
    app.post('/users/new/', callback=user_action.create_user)
    auth_required(app.put('/users/update/', callback=user_action.update_user))
    auth_required(app.get('/users/view/', callback=user_action.view_user))


def create_task_route(app: Bottle):
    auth_required(app.get('/tasks/', callback=task_action.list_task))
    auth_required(app.get('/tasks/active/', callback=task_action.list_active))
    auth_required(app.get('/tasks/closed/', callback=task_action.list_closed))
    auth_required(app.post('/tasks/new/', callback=task_action.create_task))
    auth_required(app.put('/tasks/update/', callback=task_action.update_task))

    @auth_required
    @app.get('/tasks/<task_id:int>/')
    def task_view(*args, **kwargs):
        return task_action.view_task(*args, **kwargs)


def create_routes(app: Bottle):

    create_user_route(app)
    create_task_route(app)
