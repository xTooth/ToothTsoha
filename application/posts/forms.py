from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PostForm(FlaskForm):
    content = StringField("Post content", [validators.length(min=1)])
 
    class Meta:
        csrf = False