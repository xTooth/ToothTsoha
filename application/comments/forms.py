from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CommentForm(FlaskForm):
    comment = StringField("Comment content", [validators.length(min=1)])
 
    class Meta:
        csrf = False