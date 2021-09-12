from flask import request,render_template,flash
from . import users
from .forms import RegisterForm
from .models import User #import User class from models to add informations of user to the database
from app import db #we need db Object for add and commit to database

@users.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('users/register.html',form=form)
        if not form.password.data == form.confirm_password.data:
            error_message="passwords does not match"
            form.password.errors.append(error_message)
            form.confirm_password.errors.append(error_message)
            return render_template('users/register.html',form=form)
        new_user=User()
        new_user.full_name=form.full_name.data
        new_user.email=form.email.data
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('you created your account successfully!','success')
    return render_template('users/register.html',form=form) #with form=form we can use form Object in templates file

