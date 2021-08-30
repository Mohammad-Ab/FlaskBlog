from flask import session
from . import admin


@admin.route('/')
def index():
    return "hello from admin Index"

@admin.route('/login/')
def login():
    session['name'] = 'mamad'
    #session.clear()
    #print(session.get('name'))
    print(session)
    return "1"
