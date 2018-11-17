# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv
import random

class Bus(Model):
    STOP_CODE = CharField(null=True) # IntegerField(null=True) 숫자인데 코드 앞에 0이 있어서 캐릭터로 함
    STOP_NAME = CharField(null=True)
    LONG = DoubleField(null=True)
    LAT = DoubleField(null=True)

    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database.

def table_create():
    # db_server.db_connect()

    db_server.table_create(Bus)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Bus)

def insert_interest():

    with open("C:\\yang\\bus\\BUS.csv") as data_file:
        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        reader.remove(reader[0])
        cnt = 0
        for row in reader:
            Bus.insert(STOP_CODE=row[0], STOP_NAME=row[1], LONG=row[2], LAT=row[3]).execute()


def loader():
    old_list = []

    for i in Bus.select().order_by(Bus.id).tuples():
        old_list.append(i)

    return old_list




#
#
import  random
def sample_loader(number):
    # end = math.ceil(len(Old_building().select().tuples())/100)
    old_list =[]
    rand_list = []

    for i in Bus.select().order_by(Bus.id).tuples():
        old_list.append(i)

    for j in random.sample(old_list,number):
        rand_list.append(j)

# return old_list
    return rand_list
