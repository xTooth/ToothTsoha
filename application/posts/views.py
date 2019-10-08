from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.posts.models import Post
from application.posts.forms import PostForm
from application.comments.forms import CommentForm

# handles main list of posts
@app.route("/posts", methods=["GET", "POST"])
def posts_index():
    if request.method == "GET":    
        return render_template("posts/list.html", posts = Post.query.order_by(Post.date_created.desc()).all(), form = PostForm())
        
    
    if not current_user.is_authenticated:
        return redirect("/auth/login")

    form = PostForm(request.form)    
    if not form.validate():
        return render_template("posts/list.html", form = form,  posts = Post.query.order_by(Post.date_created.desc()).all())
    
    p = Post(form.content.data)
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("posts_index"))

# handles any one specific post
@app.route("/posts/specific/<post_id>")
def post_specific(post_id):
    return render_template("posts/post.html", form = PostForm(), post = Post.query.get(post_id), commentform = CommentForm())

# handles editing of posts
@app.route("/posts/<post_id>/", methods=["POST"])
def post_edit(post_id):
    form = PostForm(request.form)

    if not form.validate():
        return render_template("/posts/post.html", form = form, post = Post.query.get(post_id), commentform = CommentForm())
    p = Post.query.get(post_id)
    p.content = form.content.data
    db.session().commit()
  
    return redirect(url_for('post_specific', post_id=post_id))

# handles deletion of posts
@app.route("/posts/specific/<post_id>/<site>/delete", methods=["POST"])
def post_delete(post_id, site):     
    p = Post.query.get(post_id)
    u = p.account_id
    
    db.session().delete(p)
    db.session().commit()
    if site == "user":
        return redirect(url_for("user_page",user_id=u))  
    return redirect(url_for("posts_index"))

# handles followed posts
@app.route('/curated', methods=["GET"])
@login_required
def posts_curated():
    posts = current_user.get_followed_posts()
    return render_template('posts/curatedPosts.html', posts = posts)
