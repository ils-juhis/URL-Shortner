from mongoengine import Document, StringField, DateTimeField, UUIDField

class Role(Document):
    id = UUIDField(primary_key=True)
    name = StringField(max_length=50, unique=True, required=True)
    description = StringField()
    created_at = DateTimeField()
