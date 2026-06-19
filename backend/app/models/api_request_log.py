from mongoengine import Document, StringField, DateTimeField, UUIDField, IntField, LongField

class ApiRequestLog(Document):
    id = LongField(primary_key=True)
    api_key_id = UUIDField(required=True)
    endpoint = StringField()
    request_method = StringField(max_length=20)
    response_status = IntField()
    response_time_ms = IntField()
    created_at = DateTimeField()
