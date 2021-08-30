from flask import Blueprint

#if we import admin_index here we get an error >  circular import/circular dpendency ERROR
admin = Blueprint('admin',__name__,url_prefix='/admin/') #make an object from Blueprint class the parameter like this (name,import name,)

from .views import index
#@admin.route('/')    move this view to views.py
#def admin_index():
    #return "hello from admin index"


