import collections
from math import ceil

from django.core.paginator import Paginator, Page as BasePage
from django.db.models.query import QuerySet
from django.utils import six


LOWER_THAN = 'lt'
GREATER_THAN = 'gt'


class InvalidTimestamp(Exception):
    pass


"""
This code assumes queryset will be given with descending `timestamp` order
This assumption is everything for us.
"""


class TimestampPaginator(Paginator):

    def __init__(self, queryset, timestamp_field, per_page, allow_empty_first_page=True):
        assert isinstance(queryset, QuerySet), '`queryset` param needs to be instance of Django Queryset'
        super(TimestampPaginator, self).__init__(queryset, per_page, allow_empty_first_page=allow_empty_first_page)
        self.timestamp_field = timestamp_field
        self.queryset = queryset
        self.allow_empty_first_page = allow_empty_first_page

    def validate_timestamp(self, ts):
        pass

    def page(self, max_timestamp=None, min_timestamp=None):
        self.validate_timestamp(max_timestamp or min_timestamp)

        timestamp_query = '{timestamp_field}__{condition}'
        timestamp_query = timestamp_query.format(timestamp_field=self.timestamp_field,
                                                 condition=GREATER_THAN if min_timestamp else LOWER_THAN)
        timestamp_query_kwarg = {timestamp_query: min_timestamp or max_timestamp}
        filtered_queryset = self.queryset._clone().filter(**timestamp_query_kwarg)

        return Page(filtered_queryset[:self.per_page + 1], self)


class Page(BasePage):

    def __init__(self, object_list, paginator):
        self.paginator = paginator
        self._has_next = len(self.object_list) > self.paginator.per_page
        self.object_list = object_list[:self.paginator.per_page]

    def has_next(self):
        return self._has_next

    def __getitem__(self, index):
        if not isinstance(index, (slice,) + six.integer_types):
            raise TypeError
        # The object_list is converted to a list so that if it was a QuerySet
        # it won't be a database hit per __getitem__.
        if not isinstance(self.object_list, list):
            self.object_list = list(self.object_list)
        return self.object_list[index]