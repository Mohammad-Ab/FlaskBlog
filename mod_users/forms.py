from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #here write our field we need them.
    email = EmailField(validators=[DataRequired()])  #they give a parameter for validators
    password = PasswordField(validators=[DataRequired()])
    
