from flask import session,render_template,request,abort,flash
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin
from .utils import admin_only_view


@admin.route('/')
@admin_only_view  #using decorator fuction
def index():
   # if session.get('user_id') is None:  this state is without decorator
       # abort(401)
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
        if not user.is_admin():
            flash('incorrect credentials',category='error')
            return render_template('admin/login.html',form=form)
        session['email'] = user.email
        session['user_id']= user.id
        session['role']= user.role
        return "logged in successfully"
    if session.get('role') == 1:
        return "you are already logged in !!!"


    return render_template('admin/login.html',form=form) #geting form as parameter to render_template to using that in the template

