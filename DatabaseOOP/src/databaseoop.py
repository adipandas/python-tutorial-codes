'''
Created on Aug 9, 2017

@author: sayalik157
'''

import sqlite3      # python lib for sqlite3 database handling 

class database:
    def __init__(self, **kwargs):
        # note: because of decorators _filename and _table are set from filename and file respectively
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')     # default tablename set as 'test'
        
    def sql_do(self, sql, *params): 
        # arbitrary number of *params are given incase more parameters are needed for 'sql' command
        self._db.execute(sql, params)   # execute sql command on database
        self._db.commit()

    def insert(self, row):      # inserting a row in database
        self._db.execute('insert into {} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1']))
        self._db.commit()
        
    def retrieve(self, key):                # to retrieve a row from database
        cursor = self._db.execute('select * from {} where t1 = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())      # fetch only one in dictionary form
    
    def update(self, row):          # to update a row in database
        self._db.execute('update {} set i1 = ? where t1=?'.format(self._table), (row['i1'], row['t1']))
        self._db.commit()
        
    def delete(self, key):
        self._db.execute('delete from {} where t1 = ?'.format(self._table), (key,))
        
    def display_rows(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            print('{}:{}'.format(row['t1'], row['i1']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by t1'.format(self._table))
        for row in cursor:
            yield dict(row)
        
    @ property          # filename getter decorator
    def filename(self): return self._filename
    
    @filename.setter    # filename setter decorator
    def filename(self, filename):
        self._filename = filename
        self._db = sqlite3.connect(self._filename)
        self._db.row_factory = sqlite3.Row
    
    @filename.deleter   # filename deleter decorator
    def filname(self): self.close()     # close the database
    
    @property       #decorator to get tablename
    def table(self): return self._table
    @table.setter   # decorator to set tablename
    def table(self, t): self._table = t
    @table.deleter  # decorator to delete tablename
    def table(self): self._table = 'test'

    def close(self):
            self._db.close()    # close the database
            del self._filename
            
def main():
    db = database(filename = 'test.db', table = 'test')

    print('Create table test')
    db.sql_do('drop table if exists test')
    db.sql_do('create table test ( t1 text, i1 int )')

    print('Create rows')
    db.insert(dict(t1 = 'one', i1 = 1))
    db.insert(dict(t1 = 'two', i1 = 2))
    db.insert(dict(t1 = 'three', i1 = 3))
    db.insert(dict(t1 = 'four', i1 = 4))
    for row in db: print(row)

    print('Retrieve rows')
    print(db.retrieve('one'), db.retrieve('two'))

    print('Update rows')
    db.update(dict(t1 = 'one', i1 = 101))
    db.update(dict(t1 = 'three', i1 = 103))
    for row in db: print(row)

    print('Delete rows')
    db.delete('one')
    db.delete('three')
    for row in db: print(row)

    print('Done!!')
if __name__ == '__main__':main()