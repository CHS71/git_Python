# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv
import random


class Comm_reg(Model):
    # 순번 = IntegerField(null=True)
    TRD_ID = IntegerField(null=True)
    TRD_NM = CharField(null=True)
    SHAPE_AREA =  DoubleField(null=True)
    LONG= DoubleField(null=True)
    LAT = DoubleField(null=True)

    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database

def table_create():
    # db_server.db_connect()

    db_server.table_create(Comm_reg)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Comm_reg)

def insert_interest():

    with open("C:\\yang\\comm_reg_0\\COMM_REG.csv") as data_file:

        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        reader.remove(reader[0])
        for row in reader:
            Comm_reg.insert(TRD_ID =row[0], TRD_NM=row[1],SHAPE_AREA=row[2],LONG=row[3], LAT=row[4] ).execute()




def loader():
    old_list = []

    for i in Comm_reg.select().order_by(Comm_reg.id).tuples():
        old_list.append(i)

    return old_list




#
#

def sample_loader(number):
    # end = math.ceil(len(Old_building().select().tuples())/100)
    old_list =[]
    rand_list = []

    for i in Comm_reg.select().order_by(Comm_reg.id).tuples():
        old_list.append(i)

    for j in random.sample(old_list,number):
        rand_list.append(j)

# return old_list
    return rand_list