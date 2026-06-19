from mongoengine import Document, StringField, DateTimeField, UUIDField, BooleanField

class Notification(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    title = StringField(max_length=255)
    message = StringField()
    type = StringField(max_length=50)
    is_read = BooleanField(default=False)
    created_at = DateTimeField()
