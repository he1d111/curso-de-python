from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Albums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    artist = db.Column(db.String(30))
    year = db.Column(db.Date())
    price = db.Column(db.Integer())