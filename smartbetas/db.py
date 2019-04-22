# -*- coding: UTF-8 -*-
from pydal import DAL, Field
import os

os.mkdir('db') if not os.path.isdir('db') else None
# DB file definition
folder = os.getcwd()+('/db' if os.name != 'nt' else '\db')
db = DAL('sqlite://storage.sqlite', folder=folder, migrate_enabled=True)

db.define_table('investments',
                Field('date', 'datetime'),
                Field('name', 'string'),
                Field('vol', 'json'),
                Field('cmr', 'json'),
                Field('cmp', 'json'),
                Field('prc', 'json'))

db.define_table('portfolios',
                Field('date', 'datetime'),
                Field('name', 'string'),
                Field('vol', 'json'),
                Field('cmr', 'json'),
                Field('cmp', 'json'),
                Field('prc', 'json'))

db.define_table('symbols',
                Field('ticker', 'string'),
                Field('name', 'string'))

db.define_table('price',
                Field('date', 'datetime'),
                Field('ticker', 'string'),
                Field('price', 'float'))

db.define_table('checks',
                Field('name', 'string'),
                Field('vol', 'json'),
                Field('cmr', 'json'),
                Field('cmp', 'json'),
                Field('date', 'string'))
