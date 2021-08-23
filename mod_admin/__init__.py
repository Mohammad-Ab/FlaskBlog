from flask import Blueprint


admin = Blueprint('admin',__name__,url_prefix='/admin/') #make an object from Blueprint class the parameter like this (name,import name,)

@admin.route('/')
def admin_index():
    return "hello from admin index"


