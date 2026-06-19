from mongoengine import Document, StringField, UUIDField

class Tag(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    name = StringField(max_length=100)
