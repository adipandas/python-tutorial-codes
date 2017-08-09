'''
Created on Aug 8, 2017

@author: Aditya


This program gives demo for Database useage in python
'''
import sqlite3      # import python library that supports sqlite3

def create_database(filename):
    db = sqlite3.connect(filename)      # connects the file and creates the database if it did not exist
    return db

def readwrite_database():
    filename = 'demo.db'    # database filename
    db = create_database(filename)
    db.execute('drop table if exists testtable')     # to remove table of name 'testtable' if existing
    db.execute('create table testtable (t1 text, i1 int)')  # create table 'testtable' with columns (t1,i1)=(text,int)
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('one', 1)) # insert values in columns (t1,i1) of database testtable
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('four', 4))
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('five', 5))
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('six', 6))
    db.commit()     # commit after changing any data in database
    
    cursor = db.execute('select * from testtable order by t1')  # select data from testtable in order of t1 column
    for row in cursor:
        print(row)
        
    cursor = db.execute('select i1, t1 from testtable order by i1') # select data from testtable in order of i1 column and also change the order of display
    for row in cursor:
        print(row)

def using_rowfactory():
    filename = 'demo.db'    # database filename
    db = create_database(filename)
    db.row_factory = sqlite3.Row
    db.execute('drop table if exists testtable')            # to remove table of name 'testtable' if existing
    db.execute('create table testtable (t1 text, i1 int)')  # create table 'testtable' with columns (t1,i1)=(text,int)
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('one', 1)) # insert values in columns (t1,i1) of database testtable
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('four', 4))
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('five', 5))
    db.execute('insert into testtable (t1, i1) values (?, ?)', ('six', 6))
    db.commit()     # commit after changing any data in database
    
    cursor = db.execute('select * from testtable order by t1')  # select data from testtable in order of t1 column
    for row in cursor:
        print(row)
    print('Notice: the iterator returns row objects. Read these row objects as dictionaries.')
    
    cursor = db.execute('select * from testtable order by t1')  # select data from testtable in order of t1 column
    for row in cursor:
        print(dict(row))
        
    cursor = db.execute('select * from testtable order by t1')  # select data from testtable in order of t1 column
    for row in cursor:
        print(row['t1'])
        print(row['t1'], row['i1'])
        

def main():
    readwrite_database()
    using_rowfactory()
    
if __name__ == '__main__':main()