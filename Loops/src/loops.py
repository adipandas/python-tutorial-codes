'''
Created on Jul 29, 2017

@author: Aditya
This program introduces and gives examples about various loops in python

Note : In python all the container types are iterators
'''

def while_loop():
    print('while loop demonstrated using fibonacci series:')
    a, b = 0, 1
    while b<60:
        print(b, end=' ')
        a, b = b, a+b
        
def for_loop():
    print('for_loop demonstration through file reading:')
    
    fh = open('demo.txt')   # create a file handle and open the file to read
    
    # fh.readlines() is an iterator 
    for line in fh.readlines():
        print(line, end='')
        
def enumerating_demo():
    print('Demonstrating enumeration in python and accessing the index of the element index from a container object:')
    fh = open('demo.txt')
    for idx, lines in enumerate(fh.readlines()):
        print(idx, lines, end='')
    
    print()
    
    s = 'Iterating over a string'
    print(s)
    for i, c in enumerate(s):
        if c=='i': print('index {} is an \'i\''.format(i))
    
def loop_control():
    print('Demonstrating loop control in python.')
    print('Use of \'continue\' keyword in python: ')    
    s = 'University of Cincinnati'
    print(s)
    
    for i in s:
        if i=='i': continue
        print(i, end='')
    print('\n\'Continue\' keyword skips the character \'i\' and continues to next character')
    
    print()
    print('Use of \'break\' keyword:')
    for i in s:
        if i =='i': break
        print(i, end='')
    print('\nNotice that \'break\' keyword terminates the loop with first appearance of \'i\' in the loop.')
    
    
    print('\nUse of \'else\' with for_loop')
    for i in s:
        print(i, end='')
    else:
        print('\nThis is printed because of the end of for_loop.')
    
    print('''Note that loop control keywords, 'continue', 'break' and 'else', work in the similar way with while loop as well.
If one notices below the use of \'else\' keyword with while as a demo.''')
    
    i=0
    while i<len(s):
        print(s[i], end='')
        i+=1
    else:
        print('\nWhile loop ended.')
    
def main():
    while_loop()
    
    print('') # to print empty line
    
    for_loop()
    
    print('')
    
    enumerating_demo()
    
    print('')
    
    loop_control()

if __name__ == '__main__':main()