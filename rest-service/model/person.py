from dbflasksqlalchemy import db

# Mapping between a raw in a table and a Python object
class PersonModel(db.Model):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(25), unique=True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    # orders = db.relationship("OrderModel", back_populates = "person", lazy = "dynamic")