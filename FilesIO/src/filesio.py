'''
Created on Aug 8, 2017

@author: Aditya

This program demonstrates the python IO capabilities.

File reading and writing for text and binary files are demonstrated.
'''

def readfiledemo():
    f = open('smallfile.txt')
    for line in f:
        print(line, end='')
        
def readwritefiledemo():
    fin = open('smallfile.txt', 'r')
    fout = open('demofile1.txt', 'w')
    for line in fin:
        print(line, file = fout, end = '')
        
def bigfiledemo():
    fin= open('largefile.txt','r')
    fout = open('demofile2.txt','w')    # open demofile to wite
    buffersize = 50000                  # buffer size in bytes
    
    buffer = fin.read(buffersize)
    
    print('Read method on file handle object is not iterable. Therefore, using while-loop and not for-loop.')
    while len(buffer):
        fout.write(buffer)
        print('.', end='')
        buffer = fin.read(buffersize)
        
    print('\nDone writing the big file.')
    
def readwritebinaryfilesdemo():
    fin = open('ants.jpg','rb')     # read binary
    fout = open('demo.jpg','wb')    # write binary
    buffersize = 50000  # buffer in bytes
    buffer = fin.read(buffersize)
    print('Note: Image read in binary format.')
    print(buffer)
    while len(buffer):
        fout.write(buffer)
        print('.',end='')
        buffer = fin.read(buffersize)
    print('\nDone writing the image.')
    
def main():
    #writebigfile()
    readwritebinaryfilesdemo()
    readfiledemo()
    readwritefiledemo()
    bigfiledemo()
    
    
    
def writebigfile():
    f = open('largefile.txt', 'w')
    for i in range(10000):
        print('{:05} Yo the big file of the Files'.format(i), file=f)
    print('Done writing.')

if __name__ == '__main__':main()