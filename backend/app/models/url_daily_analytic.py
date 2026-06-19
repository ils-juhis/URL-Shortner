from mongoengine import Document, DateTimeField, UUIDField, LongField, DateField

class UrlDailyAnalytic(Document):
    id = LongField(primary_key=True)
    url_id = UUIDField(required=True)
    analytics_date = DateField()
    total_clicks = LongField()
    unique_clicks = LongField()
    created_at = DateTimeField()
