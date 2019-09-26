from application import db
from sqlalchemy.sql import text

class Post(db.Model):
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