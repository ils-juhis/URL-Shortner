from mongoengine import Document, StringField, DateTimeField, UUIDField

class UserSession(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    refresh_token = StringField(required=True)
    ip_address = StringField(max_length=100)
    user_agent = StringField()
    device = StringField(max_length=100)
    browser = StringField(max_length=100)
    os = StringField(max_length=100)
    expires_at = DateTimeField()
    created_at = DateTimeField()
