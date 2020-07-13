import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

COOKIES_SECRET = ""

SECRET = "Insira aqui o seu segredo."

JWT_SECRET = "Insira aqui o seu segredo para token."

DATE_FORMAT = "%d-%m-%Y"

DATETIME_FORMAT = "%d-%m-%Y %H%M%S"

STATIC_PATH = os.path.join(ROOT_PATH, 'statics')
