from mongoengine import Document, StringField, DateTimeField, UUIDField, BooleanField

class PasswordReset(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    token = StringField(max_length=255)
    expires_at = DateTimeField()
    used = BooleanField(default=False)
    created_at = DateTimeField()
