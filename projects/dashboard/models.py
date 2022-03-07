from datetime import datetime

from projects import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    link = db.Column(db.String(255))
    price = db.Column(db.String(30))
    rating = db.Column(db.String(30))
    created = db.Column(db.Datetime, default=datetime.now())

    def __init__(self, id, title, link, price, rating) -> None:
        self.id = id
        self.title = title
        self.link = link
        self.price = price
        self.rating = rating

        
