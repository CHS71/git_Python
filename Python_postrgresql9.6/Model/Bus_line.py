# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv
import  random

class Bus_line(Model):
    BUS_NUM = CharField(null=True)
    STOP_CODE = CharField(null=True) # IntegerField(null=True) 숫자인데 코드 앞에 0이 있어서 캐릭터로 함
    STOP_NAME = CharField(null=True)

    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database.

def table_create():
    # db_server.db_connect()

    db_server.table_create(Bus_line)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Bus_line)

def insert_interest():

    with open("C:\\yang\\bus\\BUS_LINE.csv", encoding="utf-8") as data_file:
        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        reader.remove(reader[0])
        cnt = 0
        for row in reader:
            Bus_line.insert(BUS_NUM=row[1], STOP_CODE=row[4], STOP_NAME=row[5]).execute()




def loader():
    old_list = []

    for i in Bus_line.select().order_by(Bus_line.id).tuples():
        old_list.append(i)

    return old_list




#
#

def sample_loader(number):
    # end = math.ceil(len(Old_building().select().tuples())/100)
    old_list =[]
    rand_list = []

    for i in Bus_line.select().order_by(Bus_line.id).tuples():
        old_list.append(i)

    for j in random.sample(old_list,number):
        rand_list.append(j)

# return old_list
    return rand_list