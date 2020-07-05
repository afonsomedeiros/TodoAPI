from bottle import Bottle
from .actions import user_action

def create_routes(app: Bottle):

    app.get('/users/', callback=user_action.list_user)
    #app.get('/users/<user_id:int>/')
    #def user_update(*args, **kwargs):
    #    return user_action.view_user(*args, **kwargs)
    #app.post('/users/new/', callback=user_action.create_user)

    #@app.put('/users/update/<user_id:int>/')
    #def user_update(*args, **kwargs):
    #    return user_action.update_user(*args, **kwargs)

    #@app.delete('/users/delete/<user_id:int>/')
    #def user_update(*args, **kwargs):
    #    return user_action.delete_user(*args, **kwargs)
