from mongoengine import Document, StringField, DateTimeField, UUIDField, BooleanField

class ApiKey(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    name = StringField(max_length=255)
    api_key_hash = StringField()
    is_active = BooleanField(default=True)
    expires_at = DateTimeField()
    last_used_at = DateTimeField()
    created_at = DateTimeField()
