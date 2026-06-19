from mongoengine import Document, UUIDField

class UrlTag(Document):
    url_id = UUIDField(required=True)
    tag_id = UUIDField(required=True)

    meta = {
        'indexes': [
            {'fields': ('url_id', 'tag_id'), 'unique': True}
        ]
    }
