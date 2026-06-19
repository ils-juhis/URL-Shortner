from mongoengine import Document, UUIDField

class RolePermission(Document):
    role_id = UUIDField(required=True)
    permission_id = UUIDField(required=True)

    meta = {
        'indexes': [
            {'fields': ('role_id', 'permission_id'), 'unique': True}
        ]
    }
