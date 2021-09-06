from flask import session,render_template,request,abort,flash
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin


@admin.route('/')
def index():
    return "hello from admin Index"

@admin.route('/login/',methods=['GET','POST'])
def login():
    #session['name'] = 'mamad'
    #session.clear()
    #print(session.get('name'))
    #print(session)
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email.ilike(f'{form.email.data}')).first() #using ilike
        if not user:
            flash("incorrect credentials!",category='error')
            #return "incorrect credentials"
            return render_template('admin/login.html',form=form)
        if not user.check_password(form.password.data):
            flash("incorrect credentials!",category='error')
            #return "incorrect credentials"
            return render_template('admin/login.html', form=form)
        session['email'] = user.email
        session['user_id']= user.id
        return "logged in successfully"
    if session.get('email') is not None:
        return "you are already logged in !!!"


    return render_template('admin/login.html',form=form) #geting form as parameter to render_template to using that in the template

