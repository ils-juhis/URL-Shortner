from mongoengine import Document, StringField, DateTimeField, UUIDField, BooleanField

class Domain(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    domain_name = StringField(max_length=255, unique=True)
    ssl_enabled = BooleanField(default=False)
    verification_token = StringField(max_length=255)
    verification_status = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_at = DateTimeField()
