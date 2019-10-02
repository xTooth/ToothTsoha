from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CommentForm(FlaskForm):
    comment = StringField("Comment content", [validators.length(min=1), validators.length(max=144, message="Your input is too strong (too many characters max = 144)")])
 
    class Meta:
        csrf = False