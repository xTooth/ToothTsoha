from flask import redirect, render_template, request, url_for

from application import app, db
from application.posts.models import Post

@app.route("/")
def index():
   return render_template("index.html", most_commented=Post.find_most_commented_posts(), most_liked=Post.find_most_liked_posts())