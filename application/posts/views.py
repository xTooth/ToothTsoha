from application import app, db
from flask import redirect, render_template, request, url_for
from application.posts.models import Post

@app.route("/posts", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())


@app.route("/posts/new/")
def post_form():
    return render_template("posts/new.html")

@app.route("/posts/<post_id>/", methods=["POST"])
def post_set_done(post_id):

    t = Post.query.get(post_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("posts_index"))


@app.route("/posts/", methods=["POST"])
def post_create():
    t = Post(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("posts_index"))