import json
import datetime
from core.models import Users


def serializer_date(date):
    if isinstance(date, datetime.datetime) or isinstance(date, datetime.date):
        return date.__str__()


def serializer_error(err_message, err_valid_data):
    error_response = {
        'err_messages': err_message,
        'err_valid_data': err_valid_data
    }
    return json.dumps(error_response, default=serializer_date)


def remove_password(objs: list):
    for i in range(0, len(objs)):
        if isinstance(objs[i], Users):
            objs[i].password = None
        else:
            objs[i].user.password = None
    return objs