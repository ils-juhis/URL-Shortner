from mongoengine import Document, StringField, DateTimeField, UUIDField, DictField, LongField

class AuditLog(Document):
    id = LongField(primary_key=True)
    user_id = UUIDField()
    action = StringField(max_length=255)
    entity_type = StringField(max_length=100)
    entity_id = UUIDField()
    old_value = DictField()
    new_value = DictField()
    ip_address = StringField(max_length=100)
    created_at = DateTimeField()
