'''
Created on Jul 30, 2017

@author: Aditya

This program demonstrates the exception handling in python code.
'''
def read_file_n_display():
    print('Working code to read and display the file.')
    fh = open('sample.txt')
    for line in fh: print(line.strip())

def simple_exception_demo():
    try:
        fh = open('xsample.txt') # file handle
    except:
        print('Cannot open the file.')
    else:
        for line in fh:
            print(line.strip())
            
def exception_demo():
    print('Notice:\nIn try block, the code execution stops at the line where exception occurs. \
    The further code is not executed.')

    try:
        fh = open('xsample.txt')
        for line in fh: print(line.strip())
    except Exception as e:
        print('Something happened.')
        print(e)

def exception_demo_specific_exception():
    print('Demo for exception handling with specific exception.')
    try:
        fh = open('xsample.txt') # file handle
    except IOError as e:
        print('Cannot open the file.', e)
    else:
        for line in fh:
            print(line.strip())

def raise_exception_demo():
    print('Demonstration of raising an exception in python.')
    
    try:
        for line in readfile('sample.doc'): print(line.strip())
    except IOError as e:
        print('File cannot be found,', e)
    except ValueError as e:
        print('Bad filename.', e)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()   # This function returns an iterator
    else:
        raise ValueError('Filename must end with \'.txt\'. Please check the file format.')
    
def main():
    simple_exception_demo()
    print()
    exception_demo()
    print()
    exception_demo_specific_exception()
    print()
    read_file_n_display()
    print()
    raise_exception_demo()
    
if __name__ == '__main__':main()