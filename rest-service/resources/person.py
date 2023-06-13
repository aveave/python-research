from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PersonSchema
from model import PersonModel
from dbflasksqlalchemy import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Persons", "persons", description = "Persons methods")

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

class PersonBlueprint(MethodView):

    @blp.route("/persons")
    @blp.arguments(PersonSchema)
    def create_person(self, person_data):
        print(person_data)
        person = PersonModel(**person_data)
        try:
            db.session.add(person)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message = "An error occured while insert")
            # return {"message": "An error occured while ins"}, 404
        return '', 200

    @blp.route("/persons", methods = ['GET'])
    def get_all():
        persons = PersonModel.query.all()
        serialized_persons = persons_schema.dump(persons)
        return serialized_persons
    
    @blp.route('/persons/<int:id>', methods = ['GET'])
    def get_person(id):
        person = PersonModel.query.get(id)
        if person is None:
            abort(400, message = "Person with provided id is not found")
        return person_schema.dump(person)
    
    @blp.route('/persons/<int:id>', methods = ['DELETE'])
    def delete_person(id):
        person = PersonModel.query.get(id)
        if person is None:
            abort(400, message = "Person with provided id is not found")
        db.session.delete(person)
        db.session.commit()
        return {'message': 'Person deleted successfully'}