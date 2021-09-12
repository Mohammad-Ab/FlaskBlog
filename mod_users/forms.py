from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField,StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #here write our field we need them.
    email = EmailField(validators=[DataRequired()])  #they give a parameter for validators
    password = PasswordField(validators=[DataRequired()])

class RegisterForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])
    full_name = StringField() #it's not necessary so does'nt need validators
