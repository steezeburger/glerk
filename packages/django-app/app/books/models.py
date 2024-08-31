from django.db import models

from common.models.crud_timestamps_mixin import CRUDTimestampsMixin
from common.models.soft_delete_timestamp_mixin import SoftDeleteTimestampMixin
from common.models.uuid_mixin import UUIDModelMixin


class Book(UUIDModelMixin, SoftDeleteTimestampMixin, CRUDTimestampsMixin):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField(null=True)
    cover_url = models.URLField(null=True)
    # TODO - add author model. starting simple for now.
    author = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'books'
        default_permissions = ()
        ordering = ('id',)

    def __str__(self):
        return self.title
