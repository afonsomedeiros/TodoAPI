import datetime


def serializer_date(date):
    if isinstance(date, datetime.datetime) or isinstance(date, datetime.date):
        return date.__str__()
