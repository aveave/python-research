from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PersonSchema
from model import PersonModel
from dbflasksqlalchemy import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Persons", "persons", description = "Persons methods")

@blp.route("/persons")
class PersonBlueprint(MethodView):

    @blp.arguments(PersonSchema)
    def post(self, person_data):
        print(person_data)
        person = PersonModel(**person_data)
        try:
            db.session.add(person)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message = "An error occured while ins")
            # return {"message": "An error occured while ins"}, 404
        return '', 200

    def get(self):
        print('bbbb')
        persons = PersonModel.query.all()
        print('persons aree ', persons)
        return persons

# @app.route('/persons/<id>', methods = ['GET'])
# def get_person_by_id(id):
#     result = db.get_note_by_id_from_db(id)
#     return jsonify(result)