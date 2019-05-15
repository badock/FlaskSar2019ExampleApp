from database.database import db


class Engineer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    site = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Engineer {}>'.format(self.username)
