from flask import Blueprint

users = Blueprint('users',__name__,url_prefix='/users/')

from .models import User #import class User from models.py file

from . import views


