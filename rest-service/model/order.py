from dbflasksqlalchemy import db

class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable = False)
    person_id = db.Column(db.Integer, db.ForeignKey("persons.id"), unique = False, nullable = False)
    person = db.relationship("PersonModel", back_populates = "persons")