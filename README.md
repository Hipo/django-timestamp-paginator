# TimestampPaginator

Django Timestamp Paginator

## Installation

`pip install django-timestamp-paginator`

## Usage

```python
from django_timestamp_paginator import TimestampPaginator

queryset = MyModel.objects.all()  # A queryset ordered by my timestamp field (ASC or DESC)
my_timestamp_field = 'timestamp'  # My model has a field named timestamp 
results_per_page = 30  # I want to see 30 results per page

paginator = TimestampPaginator(queryset, my_timestamp_field, results_per_page)

page = paginator.page()  # Get me the first page, regarding queryset ordering

repr(page)
>>> <Page with next timestamp=1425028897.60>

next_page_timestamp = page.next_page_timestamp()
next_page = paginator.page(timestamp=next_page_timestamp)

```

### Previous Page?
No, there is no previous page. TimestampPaginator goes **only forwards** , ***regarding queryset ordering***. If you want to fetch latest results, go ahead and get first page by `paginator.page()`

### Requirements

Django

------------------------
Thanks to @yigitguler and whole @Hipo team for inspiration and contributions.

![Hipo](https://avatars1.githubusercontent.com/u/1497148?v=3&s=50)
