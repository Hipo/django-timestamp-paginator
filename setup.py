from distutils.core import setup
#TODO
setup(
    name='django-rest-framework-mongoengine',
    version='2.0.2',
    description='MongoEngine support for Django Rest Framework.',
    packages=['rest_framework_mongoengine',],
    license='see https://github.com/umutbozkurt/django-rest-framework-mongoengine/blob/master/LICENSE',
    long_description='see https://github.com/umutbozkurt/django-rest-framework-mongoengine/blob/master/README.md',
    url='https://github.com/umutbozkurt/django-rest-framework-mongoengine',
    download_url='https://github.com/umutbozkurt/django-rest-framework-mongoengine/releases/',
    keywords=['mongoengine', 'serializer', 'django rest framework'],
    author='Umut Bozkurt',
    author_email='umutbozkurt92@gmail.com',
    requires=['mongoengine', 'djangorestframework'],
    classifiers=['Development Status :: 5 - Production/Stable',
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
