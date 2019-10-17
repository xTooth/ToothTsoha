from application import db
from sqlalchemy.sql import text


#associationtable between users and posts or "likes"
likes = db.Table(
   "likes",
   db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
   db.Column("liker_id", db.Integer, db.ForeignKey("account.id"))
)

class Post(db.Model):
    #again has to be here due to association table.
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    content = db.Column(db.String(144), nullable=False)
 
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    comments = db.relationship("Comment", backref='post', cascade="all, delete, delete-orphan", lazy=True)
    
    def __init__(self, contnet):
        self.content = contnet
    
    liked = db.relationship(
        "User",
        secondary=likes,
        backref=db.backref("likes",lazy='dynamic'),
        lazy='dynamic'
        )
    #Find most posts with the largerst amount of comments.
    @staticmethod
    def find_most_commented_posts():
        stmt = text("SELECT id, content"
                    " FROM post AS p"
                    " INNER JOIN( SELECT post_id, COUNT(*) AS postcount FROM comment"
                    " GROUP BY post_id) AS c"
                    " ON p.id = c.post_id"
                    " ORDER BY c.postcount DESC LIMIT 5")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0],"content":row[1]})

        return response

    @staticmethod
    def find_most_liked_posts():
        stmt = text("SELECT id, content"
                    " FROM post AS p"
                    " INNER JOIN( SELECT post_id, COUNT(*) AS likecount FROM likes"
                    " GROUP BY post_id) AS l"
                    " ON p.id = l.post_id"
                    " ORDER BY l.likecount DESC LIMIT 5")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0],"content":row[1]})

        return response