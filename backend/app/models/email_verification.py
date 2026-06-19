from mongoengine import Document, StringField, DateTimeField, UUIDField

class EmailVerification(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    token = StringField(max_length=255)
    expires_at = DateTimeField()
    verified_at = DateTimeField()
