from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.comments.models import Comment
from application.comments.forms import CommentForm
from application.posts.forms import PostForm
from application.posts.models import Post

#comment creation
@app.route("/posts/specific/<post_id>", methods=["POST"])
@login_required
def new_comment(post_id):
    
    form = CommentForm(request.form)
    if not form.validate():
        return render_template("/posts/post.html", form = PostForm(), post = Post.query.get(post_id), commentform = form)
    
    c = Comment(form.comment.data)
    c.account_id = current_user.id
    c.post_id = post_id
    
    db.session.add(c)
    db.session.commit()

    return redirect(url_for('post_specific', post_id=post_id))

#comment editing
@app.route("/posts/specific/<post_id>/<comment_id>/edit", methods=["POST"])
@login_required
def comment_edit(post_id, comment_id):
    form = CommentForm(request.form)
    if not form.validate():
        return render_template("/posts/post.html", form = PostForm(), post = Post.query.get(post_id), commentform = form)
    c = Comment.query.get(comment_id)
    if c.account_id == current_user.id:
        c.content = form.comment.data
        db.session().commit()
  
    return redirect(url_for('post_specific', post_id=post_id))

# comment deletion
@app.route("/posts/specific/<post_id>/<comment_id>/deleteComment", methods=["POST"])
@login_required
def comment_delete(post_id, comment_id):     
    c = Comment.query.get(comment_id)
    if c.account_id == current_user.id:
        db.session().delete(c)
        db.session().commit()  
    return redirect(url_for('post_specific', post_id=post_id))