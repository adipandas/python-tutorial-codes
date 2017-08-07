'''
Created on Aug 6, 2017

@author: Aditya

This program explains the details of generator objects.
'''

class inclusive_range:
    def __init__(self, *args):     # this method is constructor
        nargs = len(args)
        if nargs<1: raise TypeError('Requires atleast one argument.')
        elif nargs==1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif nargs==2:
            self.start, self.stop = args
            self.step = 1
        elif nargs==3:
            self.start, self.stop, self.step = args
        else: raise TypeError('Expected atmost 3 arguments. Got {} arguments.'.format(nargs))
    
    def __iter__(self):     
        # this method creates the iterator object and we can thus put our generator function over here.
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step
            
def main():
    o = range(25)   # range object
    print('Type of range object: ', type(o))
    for i in o: print(i, end=' ')   # range object used in context of iterator
    print('\nNote: range object is a generator.')
    print('Also range is exclusive iterator, i.e., it excludes the upper limit.')
    
    print()
    print('Illustrating Generator Object in Python.')
    o = inclusive_range(25)
    for i in o: print(i, end = ' ')
    print()
    
if __name__ == '__main__':main()