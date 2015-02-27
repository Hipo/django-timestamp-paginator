import sys

from django.core.paginator import Paginator, Page as BasePage
from django.db.models.query import QuerySet
from django.utils import six
from django.utils.encoding import smart_str


LOWER_THAN = 'lt'
GREATER_THAN = 'gt'

ASCENDING = ''
DESCENDING = '-'


class InvalidTimestamp(Exception):
    pass


class TimestampPaginator(Paginator):

    def __init__(self, queryset, timestamp_field, per_page, allow_empty_first_page=True):
        assert isinstance(queryset, QuerySet), '`queryset` param needs to be instance of Django Queryset'
        super(TimestampPaginator, self).__init__(queryset, per_page, allow_empty_first_page=allow_empty_first_page)
        self.timestamp_field = timestamp_field
        self.queryset = queryset
        self.ordering = self._get_ordering()
        assert self.ordering is not None, '`queryset` must be ordered by ' \
                                          '`{ts_field}` or `-{ts_field}`'.format(ts_field=self.timestamp_field)

        self.allow_empty_first_page = allow_empty_first_page

    def validate_timestamp(self, ts):
        pass

    def _get_ordering(self):
        for order in self.queryset.query.order_by + list(self.queryset.model._meta.ordering):
            if order == DESCENDING + self.timestamp_field:
                return DESCENDING
            elif order == ASCENDING + self.timestamp_field:
                return ASCENDING
            else:
                continue

    def page(self, timestamp=None):
        if not timestamp:
            timestamp = sys.float_info.max if self.ordering == DESCENDING else sys.float_info.min
        else:
            self.validate_timestamp(timestamp)

        timestamp_query = '{timestamp_field}__{condition}'
        condition = GREATER_THAN if self.ordering == ASCENDING else LOWER_THAN
        timestamp_query = timestamp_query.format(timestamp_field=self.timestamp_field,
                                                 condition=condition)

        timestamp_query_kwarg = {timestamp_query: timestamp}
        filtered_queryset = self.queryset.filter(**timestamp_query_kwarg)

        return Page(filtered_queryset[:self.per_page + 1], self)


class Page(BasePage):

    def __init__(self, object_list, paginator):
        self.paginator = paginator
        self._has_next = len(object_list) > self.paginator.per_page
        self.object_list = object_list[:self.paginator.per_page]

    def has_next(self):
        return self._has_next

    def has_previous(self):
        """
        Not implemented
        """
        return False

    def next_page_timestamp(self):
        return getattr(self.object_list[-1], self.paginator.timestamp_field)

    def __repr__(self):
        return '<Page with next timestamp=%s>' % smart_str(self.next_page_timestamp())