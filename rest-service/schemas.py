from marshmallow import Schema, fields

class PersonSchema(Schema):
    id = fields.Str(dump_only=True)
    login = fields.Str(required=True)
    name = fields.Str(required=True)
