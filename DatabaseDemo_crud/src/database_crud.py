'''
Created on Aug 9, 2017

@author: Aditya

This file gives the demonstration of 4 basic and most important function of database
CRUD :: Create - Retrieve - Update - Delete 
'''

import sqlite3  # import python database lib

def insert(db, row):    # function to insert rows in database
    # db - database object
    # row - row to be inserted in the database
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))   # insert row into the database
    db.commit()


def display_rows(db):           # function to display rows from database
    # db - database object
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('{}:{}'.format(row['t1'],row['i1']))
        
def retrieve_row(db, key):      # to retrieve data from database
    cursor = db.execute('select * from test where t1 = ?', (key,))        # note that argument is passed as single element tuple
    return cursor.fetchone()        # fetch one data from database

def update_row(db, row):                    # to update row in database
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit()

def delete_row(db, key):        # to delete row from database
    db.execute('delete from test where t1 = ?', (key,))
    db.commit()

def main():
    print('Note: Call commit() on database after doing any change in it.')
    db = sqlite3.connect('TestDB.db')       # creating and connecting to test database
    db.row_factory = sqlite3.Row
    
    print('Create a table named \'test\' in the database')
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    
    print('Create Rows')
    insert(db, dict(t1 = 'one', i1 = '1'))  # insert table rows in database in dictionary form
    insert(db, dict(t1 = 'two', i1 = '2'))
    insert(db, dict(t1 = 'three', i1 = '3'))
    insert(db, dict(t1 = 'four', i1 = '4'))
    insert(db, dict(t1 = 'five', i1 = '5'))
    insert(db, dict(t1 = 'six', i1 = '6'))
    insert(db, dict(t1 = 'seven', i1 = '7'))
    display_rows(db)
    
    print('Retrieve data from database')
    print(dict(retrieve_row(db, 'one')), dict(retrieve_row(db, 'two')))
    
    print('Update row in database')
    update_row(db, dict(t1 = 'one', i1 = 101))
    update_row(db, dict(t1 = 'two', i1 = 102))
    display_rows(db)

    print('Delete rows')
    delete_row(db, 'one')
    delete_row(db, 'two')
    display_rows(db)

if __name__ == '__main__':main()