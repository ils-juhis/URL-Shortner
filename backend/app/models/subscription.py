from mongoengine import Document, StringField, DateTimeField, UUIDField

class Subscription(Document):
    id = UUIDField(primary_key=True)
    user_id = UUIDField(required=True)
    plan_id = UUIDField(required=True)
    status = StringField(max_length=50)
    started_at = DateTimeField()
    expires_at = DateTimeField()
    created_at = DateTimeField()
