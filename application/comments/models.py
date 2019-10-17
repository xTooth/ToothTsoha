from application import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    content = db.Column(db.String(144), nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __init__(self, contnet):
        self.content = contnet