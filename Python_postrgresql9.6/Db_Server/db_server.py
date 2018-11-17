# -*- coding: utf-8 -*-
from peewee import *

psql_db = PostgresqlDatabase('shk_bigdata',  # Required by Peewee.
                             user='bigdata',  # Will be passed directly to psycopg2.
                             password='',  # Ditto.
                             host='sharekim.com')

def db_connect():

    psql_db.connect()

def table_create(table):

    psql_db.create_tables([table])

def table_drop(table):

    psql_db.drop_tables([table])

