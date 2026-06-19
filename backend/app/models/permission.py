from mongoengine import Document, StringField, UUIDField

class Permission(Document):
    id = UUIDField(primary_key=True)
    code = StringField(max_length=100, unique=True)
    name = StringField(max_length=100)
    description = StringField()
