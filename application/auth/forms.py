from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import  DataRequired,EqualTo

from application import db
from application.auth.models import User

class NewUserForm(FlaskForm):

    username = StringField("Username", [validators.DataRequired(message=('Don\'t be shy!'))])
    name = StringField("Name", [validators.DataRequired(message=( 'We do need a name...'))])

    password = PasswordField('password',validators=[DataRequired(),EqualTo('password2',message='Passwords must match.')])
    password2 = PasswordField('Confirm password',validators=[DataRequired()])
    
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

