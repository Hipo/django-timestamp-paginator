from distutils.core import setup

setup(
    name='django-timestamp-paginator',
    version='0.0.1',
    description='Timestamp Paginator for Django.',
    packages=['django_timestamp_paginator', ],
    license='see licence on https://github.com/umutbozkurt/django-timestamp-paginator',
    long_description='see https://github.com/umutbozkurt/django-timestamp-paginator/blob/master/README.md',
    url='https://github.com/umutbozkurt/django-timestamp-paginator',
    download_url='https://github.com/umutbozkurt/django-timestamp-paginator/releases/',
    keywords=['django', 'timestamp', 'paginator'],
    author='Umut Bozkurt',
    author_email='umutbozkurt92@gmail.com',
    requires=['django', ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Text Processing :: Markup :: HTML',
        'Intended Audience :: Developers'
    ],
)
