import os,re
from setuptools import setup, find_packages

with open( os.path.join( os.path.dirname(__file__), 'sqlalchemy_pygresql',
                              '__init__.py' ) ) as v:
    VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)

setup(
    name = 'sqlalchemy_pygresql'
    , version = VERSION
    , description='PyGreSQL dialect for SQLAlchemy'
    , long_description=open( 'README.rst' ).read()
    , keywords='PyGreSQL PostgreSQL SQLAlchemy'
    , author='Kaolin Imago Fire'
    , author_email='sqlalchemypygresql_spam@erif.org'
    , install_requires=['pygresql >= 4.1', 'sqlalchemy >= 0.8']
    , packages = ['sqlalchemy_pygresql',]
    , url='https://github.com/kaolin/sqlalchemy-pygresql'
    , zip_safe = False
    , entry_points={
        'sqlalchemy.dialects': [
                'postgresql.pygresql = sqlalchemy_pygresql.base:PGDialect_pypostgresql'
            ]
        }
    , license='Apache 2.0'
    , classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
