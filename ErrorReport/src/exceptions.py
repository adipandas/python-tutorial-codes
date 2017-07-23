'''
Created on Jul 23, 2017

@author: Aditya
Exceptions: To report errors in python
Exceptions are Object Oriented way of reporting errors in a code
'''

import sys, os

def readfile(filename):
    try:
        fh = open(filename)     # filehandle to open a file
    except IOError as e:
        print('Something bad happen ({})'.format(e))
        exc_type, _, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]    # filename in which error occurred
        print(exc_type, fname, 'line -', exc_tb.tb_lineno)
    return fh       # return filehandle

def main():
    try:
        fh = readfile('lines.txt')
        for line in fh.readlines():
            print(line, end='')
        
        print()    
    except Exception as e:
        print('There is an error ({})'.format(e))
        exc_type, _, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]    # filename in which error occurred
        print(exc_type, fname, 'line -', exc_tb.tb_lineno)
        
    try:
        fh = readfile('lines1.txt')
        for line in fh.readlines():
            print(line, end='')
    except Exception as e:
        print('There is an error ({})'.format(e))
        exc_type, _, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]    # filename in which error occurred
        print(exc_type, fname, 'line -', exc_tb.tb_lineno)
        
if __name__ == '__main__': main()