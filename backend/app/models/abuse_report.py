from mongoengine import Document, StringField, DateTimeField, UUIDField

class AbuseReport(Document):
    id = UUIDField(primary_key=True)
    reporter_user_id = UUIDField(required=True)
    url_id = UUIDField(required=True)
    reason = StringField()
    status = StringField(max_length=50)
    reviewed_by = UUIDField()
    reviewed_at = DateTimeField()
    created_at = DateTimeField()
