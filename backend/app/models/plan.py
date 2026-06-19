from mongoengine import Document, StringField, DateTimeField, UUIDField, IntField, BooleanField, FloatField

class Plan(Document):
    id = UUIDField(primary_key=True)
    name = StringField(max_length=100)
    monthly_price = FloatField()
    yearly_price = FloatField()
    max_urls = IntField()
    max_custom_domains = IntField()
    max_api_requests = IntField()
    analytics_enabled = BooleanField()
    api_enabled = BooleanField()
    created_at = DateTimeField()
