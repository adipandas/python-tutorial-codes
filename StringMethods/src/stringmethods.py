'''
Created on Aug 7, 2017

@author: Aditya
This program explains the String methods in python 
'''

def main():
    print('In python Everything is an object.')
    print('Even the strings in python are objects.')
    
    print()
    s = 'This is a string!'
    print(s.upper())
    print('This is a string!'.upper())
    
    s = 'this is a lower case string'
    print('Lower Case string:', s)
    print('Capitalized String:', s.capitalize())
    print('Upper Case: ', s.upper())
    print('Lower case:', s.lower())
    
    s = 'This Is A Sample'
    print(s)
    print(s.swapcase())
    print('Print location of \'sam\' in string:',s.find('Sam'))
    
    print(s.replace('Sample', 'String'))
    
    s = '   There is a space at the begining and at the end.   '
    print(s)
    print(s.strip())
    print(s.rstrip())
    
    s = '       String with new line at end\n'
    print(s)
    print(s.strip())
    print(s.rstrip('\n'))
    
    s = 'This is a string'
    
    print('Check if string \'{}\'has only alpha numeric characters in it'.format(s), 'This is false as string has \'spaces\' in it.')
    print(s.isalnum())
    
    s = 'thisisastring'
    print(s)
    print('Only_alphanumeric:', s.isalnum())
    print('check only for letters in string:', s.isalpha())
    print('check if string has only digits:', s.isdigit())
    
    s = '06.3'
    print(s)
    print('check for digits string:',s.isdigit())
    print('check decimal:', s.isdecimal())
    
    s = '1223456'
    print('check for digits:', s.isdigit())
    print('check if printable:', s.isprintable())
    
    a,b = 5, 6
    print('A = {}, B = 6'.format(a, b))
    print('B = {1}, A = {0}, B = {1}'.format(a, b))
    print('A({Addo}) and B({Mado})'.format(Addo = 333, Mado = 4443))
    
     
    print()
    print('Splitting and Joining Strings:')
    s = 'This is a string.'
    a = s.split()
    print(a)
    print('Splitting at \'i\' in string: ', s.split('i'))
    
    for w in a: print(w)
    
    s1 = ':'.join(a)
    s2 = ', '.join(a)
    s3 = ' '.join(a)
    s4 = ''.join(a)
    print('{}\n{}\n{}\n{}'.format(s1,s2,s3,s4))
    
if __name__ == '__main__':main()