from data.engine import TimeStampBaseModel
from settings import SECRET

from peewee import CharField, DateField, DoesNotExist
from passlib.hash import pbkdf2_sha512 as hsh
from hashlib import md5


class Users(TimeStampBaseModel):
    name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = CharField(max_length=200)
    password = CharField(max_length=300)
    birthday = DateField()

    def gen_hash(self):
        _secret = md5(SECRET.encode()).hexdigest()
        _password = md5(self.password.encode()).hexdigest()
        self.password = hsh.hash(_secret+_password)

    def verify(self, password):
        _secret = md5(SECRET.encode()).hexdigest()
        _password = md5(password.encode()).hexdigest()
        return hsh.verify(_secret+_password, self.password)