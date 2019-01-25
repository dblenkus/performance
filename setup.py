import os.path
import setuptools

# Get the long description from the README file
with open('README.rst') as fh:
    long_description = fh.read()

# Get package metadata from '__about__.py' file
about = {}
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'lactolyse', '__about__.py')) as fh:
    exec(fh.read(), about)

setuptools.setup(
    name=about['__title__'],
    use_scm_version=True,
    description=about['__summary__'],
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__url__'],
    license=about['__license__'],
    # Exclude tests from built/installed package.
    packages=setuptools.find_packages(
        exclude=['tests', 'tests.*', '*.tests', '*.tests.*']
    ),
    package_data={
        'lactolyse': [
            'static/lactolyse/css/*.css',
            'templates/*.html',
            'templates/lactolyse/*.html',
            'templates/lactolyse/latex/*.tex',
        ]
    },
    python_requires='>=3.6, <3.7',
    install_requires=[
        'asgiref~=2.1',
        'channels~=2.1.0',
        'channels_redis~=2.1.0',
        'Django~=2.0.0',
        'django-material~=1.2.2',
        'docker~=3.0.0',
        'Jinja2~=2.10',
        'numpy~=1.14.0',
        'psycopg2-binary~=2.7.0',
    ],
    extras_require={
        'package': ['twine', 'wheel'],
        'test': [
            'black',
            'check-manifest',
            'coverage>=4.2',
            'readme_renderer',
            'setuptools_scm',
            'twine',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Other Audience',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='ftp lactate threshold',
)
