from setuptools import setup

setup(
    name='django-bourbon',
    version='3.1.8',
    url='https://github.com/benbacardi/django-bourbon',
    description='Bourbon (http://bourbon.io/) static files packaged in a django app to speed up new applications and deployment.',
    author='Ben Cardy',
    author_email='benbacardi@gmail.com',
    license='MIT',
    keywords='django sass bourbon staticfiles'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['bourbon', ],
    package_data={
        'bourbon': [
            'static/bourbon/*.scss',
            'static/bourbon/*/*.scss',
        ],
    },
    include_package_data=True,
)
