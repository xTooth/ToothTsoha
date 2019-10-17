from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PostForm(FlaskForm):
    content = StringField("Post content", [validators.DataRequired(message=('cant be empty')),validators.length(min=1), validators.length(max=144, message="Your input is too strong (too many characters max = 144)")])
 
    class Meta:
        csrf = False