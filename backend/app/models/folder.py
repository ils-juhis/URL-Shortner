from mongoengine import Document, StringField, DateTimeField, UUIDField

class Folder(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    name = StringField(max_length=255)
    description = StringField()
    created_at = DateTimeField()
