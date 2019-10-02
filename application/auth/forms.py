from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import  DataRequired,EqualTo

from application import db
from application.auth.models import User

class NewUserForm(FlaskForm):
    x = "Your input is too strong (too many characters max = 144)"

    username = StringField("Username", [validators.DataRequired(message=('Don\'t be shy!')), validators.length(max=144, message="username: " + x)])
    name = StringField("Name", [validators.DataRequired(message=( 'We do need a name...')), validators.length(max=144, message="name: " + x)])

    password = PasswordField('password',validators=[DataRequired(),EqualTo('password2',message='Passwords must match.'), validators.length(max=144, message="password: " + x)])
    password2 = PasswordField('Confirm password',validators=[DataRequired(), validators.length(max=144, message="password: " + x)])
    
    def validate_username(self, username):      
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise validators.ValidationError('Username already taken.')
    
    class Meta:
        csrf = False

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

