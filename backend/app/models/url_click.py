from mongoengine import Document, StringField, DateTimeField, UUIDField, FloatField, LongField

class UrlClick(Document):
    id = LongField(primary_key=True)
    url_id = UUIDField(required=True)
    visitor_id = StringField(max_length=255)
    ip_address = StringField(max_length=100)
    country = StringField(max_length=100)
    region = StringField(max_length=100)
    city = StringField(max_length=100)
    latitude = FloatField()
    longitude = FloatField()
    browser = StringField(max_length=100)
    browser_version = StringField(max_length=50)
    operating_system = StringField(max_length=100)
    device_type = StringField(max_length=50)
    referrer = StringField()
    clicked_at = DateTimeField()
