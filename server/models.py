from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'


from app import db  # Assuming your Flask application is named 'app'

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    # Add other columns as needed

    # Define relationships
    customer = db.relationship("Customer", back_populates="reviews")
    item = db.relationship("Item", back_populates="reviews")

    def __repr__(self):
        return f'<Review {self.id}, {self.comment}, {self.rating}>'

# Add relationship to Customer and Item models
Customer.reviews = relationship("Review", back_populates="customer")
Item.reviews = relationship("Review", back_populates="item")
