from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.posts.models import Post
from application.posts.forms import PostForm
from application.comments.forms import CommentForm

@app.route("/posts", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.order_by(Post.date_created.desc()).all(), form = PostForm())


@app.route("/posts/specific/<post_id>")
def post_specific(post_id):
    return render_template("posts/post.html", form = PostForm(), post = Post.query.get(post_id), commentform = CommentForm())

   
@app.route("/posts/<post_id>/", methods=["POST"])
def post_edit(post_id):
    form = PostForm(request.form)
    p = Post.query.get(post_id)
    p.content = form.content.data
    db.session().commit()
  
    return redirect(url_for('post_specific', post_id=post_id))

@app.route("/posts/specific/<post_id>/delete", methods=["POST"])
def post_delete(post_id):     
    p = Post.query.get(post_id)
    db.session().delete(p)
    db.session().commit()  
    return redirect(url_for("posts_index"))

@app.route("/posts/", methods=["POST"])
@login_required
def post_create():
    form = PostForm(request.form)

    if not form.validate():
        return render_template("posts/new.html" , form = form)
    
    p = Post(form.content.data)
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("posts_index"))