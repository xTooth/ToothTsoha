from application import db
from application.models import Base
from application.posts.models import Post

# association table between Users
followers = db.Table(
   "followers",
   Base.metadata,
   db.Column("follower_id", db.Integer, db.ForeignKey("account.id")),
   db.Column("followed_id", db.Integer, db.ForeignKey("account.id"))
)

class User(db.Model):

    __tablename__ = "account"  
    #association table requires that these are here?????
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    #end of sadly required copy paste.                         
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    posts = db.relationship("Post", backref='account', cascade="all, delete, delete-orphan", lazy=True)
    comments = db.relationship("Comment", backref='account',cascade="all, delete, delete-orphan", lazy=True)

    #relation between users -> followers(following you) and followed(users you follow)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), 
        lazy='dynamic')


    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    # methods for handling followers and followed users

    def check_following_status(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def add_follow(self, user):
        if not self.check_following_status(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.check_following_status(user):
            self.followed.remove(user)

    #method for getting posts by followed users
    def get_followed_posts(self):
        return Post.query.join(
            followers,
             (followers.c.followed_id == Post.account_id)).filter(
                followers.c.follower_id == self.id).order_by(
                    Post.date_modified.desc())