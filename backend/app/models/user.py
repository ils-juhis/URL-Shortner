from mongoengine import Document, StringField, BooleanField, DateTimeField, UUIDField, ReferenceField

class User(Document):
    id = UUIDField(primary_key=True)
    role_id = UUIDField(required=True)
    first_name = StringField(max_length=100)
    last_name = StringField(max_length=100)
    username = StringField(max_length=100, unique=True)
    email = StringField(max_length=255, unique=True, required=True)
    password_hash = StringField(required=True)
    profile_image = StringField()
    is_email_verified = BooleanField(default=False)
    two_factor_enabled = BooleanField(default=False)
    status = StringField(max_length=20, default='ACTIVE')
    last_login_at = DateTimeField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
