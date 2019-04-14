# -*- coding: UTF-8 -*-
from pydal import DAL, Field
import os

os.mkdir('db') if not os.path.isdir('db') else None
    # DB file definition
db = DAL('sqlite://storage.sqlite', folder='db', migrate_enabled=True)

db.define_table('sessions',
                Field('date', 'datetime'),
                Field('tickers', 'list:string'),
                Field('tsm', 'json'),
                Field('out', 'string'),
                Field('img', 'upload'))

db.define_table('symbols',
                Field('ticker', 'string'),
                Field('name', 'string'))
