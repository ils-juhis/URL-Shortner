from mongoengine import Document, StringField, DateTimeField, UUIDField, IntField, LongField

class QrCode(Document):
    id = UUIDField(primary_key=True)
    url_id = UUIDField(required=True)
    file_url = StringField()
    color = StringField(max_length=50)
    logo_url = StringField()
    size = IntField()
    scan_count = LongField(default=0)
    created_at = DateTimeField()
