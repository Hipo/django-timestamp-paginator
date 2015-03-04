# TimestampPaginator

Django Timestamp Paginator

## Why we needed this?

Classical pagination (?page=2) doesn't work properly with actively updated list pages.

####Example:
Imagine a web page where people upload their pet's pictures. 
Anyone can upload a picture anytime and it will be listed. 
The newest picture appears at the top of the page. 
When the list will be complete, the users will go to the second page (by a link or infinite loader). 
This will work fine.
However, if during this time period, a new image will be uploaded, 
the last image of the first page will become the first item of the second page.

In order to prevent this problem, there are many alternative ways that can be used. 
One of the best alternatives is to use timestamps instead of page numbers.

This paginator makes the pagination by timestamps of the items. 

## Installation

`pip install django-timestamp-paginator`

## Usage

```python
from django_timestamp_paginator import TimestampPaginator

queryset = MyModel.objects.all()  # A queryset ordered by my timestamp field (ASC or DESC)
my_timestamp_field = 'timestamp'  # My model has a field named timestamp (DecimalField)
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

### Django Rest Framework?
If you are planning to use this package with Django Rest Framework, check out the [drf-timestamp-pagination](https://github.com/Hipo/drf-timestamp-pagination) package!

### Contribution
ANY contribution is more than welcome. 
We suffered a lot because of this issue and we are willing to help anyone who tries to understand this package. 
Do not hesitate to open issues or pull requests.

Improve the blurry parts of the readme.