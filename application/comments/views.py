from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.comments.models import Comment
from application.comments.forms import CommentForm

@app.route("/posts/specific/<post_id>", methods=["POST"])
@login_required
def new_comment(post_id):
    
    form = CommentForm(request.form)
    c = Comment(form.comment.data)
    c.account_id = current_user.id
    c.post_id = post_id
    
    db.session.add(c)
    db.session.commit()

    return redirect(url_for('post_specific', post_id=post_id))

@app.route("/posts/specific/<post_id>/<comment_id>/edit", methods=["POST"])
def comment_edit(post_id, comment_id):
    form = CommentForm(request.form)
    c = Comment.query.get(comment_id)
    c.content = form.comment.data
    db.session().commit()
  
    return redirect(url_for('post_specific', post_id=post_id))

@app.route("/posts/specific/<post_id>/<comment_id>/delete", methods=["POST"])
def comment_delete(post_id, comment_id):     
    c = Comment.query.get(comment_id)
    db.session().delete(c)
    db.session().commit()  
    return redirect(url_for('post_specific', post_id=post_id))