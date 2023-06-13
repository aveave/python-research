from flask import Flask
from flask_smorest import Api
from dbflasksqlalchemy import db
from resources.person import blp as PersonBlueprint
import model

# def create_app(db_url=None):
app = Flask(__name__)
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:secret@localhost/test'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
db.init_app(app)
api = Api(app)
with app.app_context():
    db.create_all()
api.register_blueprint(PersonBlueprint)
# return app
# os.getenv("DATABASE_URL")
# initializes flask sqlalchemy extension (connect the flask app to sqlalchemy)


# @app.route('/persons', methods = ['GET'])
# def get_persons():
#     result = db.get_notes_from_db()
#     # return result
#     return jsonify(result)

# @app.route('/persons/<id>', methods = ['GET'])
# def get_person_by_id(id):
#     result = db.get_note_by_id_from_db(id)
#     return jsonify(result)