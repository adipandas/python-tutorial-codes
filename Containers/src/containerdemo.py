'''
Created on Aug 7, 2017

@author: Aditya

This program demonstrates the CONTAINERS in python
'''

def func_tuple():
    print('Demo of Tuples in python.')
    print('NOTE: Tuple is immutable object.')
    
    t = 1, 2, 3, 4      # comma separated list gives a tuple in python
    print('NOTE: Comma separation results in tuple not the paranthesis.')
    print('Tuple: ', t)
    
    print('First tuple element:', t[0])
    print('Last tuple element:', t[-1])
    print('Length  of Tuple:', len(t))
    print('Minimum:', min(t))
    print('Maximum:', max(t))
    print('Tuple with only one element:', (1,))
    print((1,), ':', type((1,)))
    
    t = tuple(range(25))
    print('tuple t:', t)
    print(type(t))
    print('Check for presence of 10 in \'t\':', (10 in t))
    print('Check for presence of 50 in \'t\':', (50 in t))
    print('Check for absence of 50 in \'t\':', (50 not in t))
    
    print('Count Number of 5s in t:', t.count(5))
    print('Index of 5 and 6 in t:', t.index(5))
    

def func_list():
    print('Demo for LISTs in python.')
    print('Note: Lists are mutable objects')
    print('Created using square brackets.')
    
    l = [1, 2, 3, 4, 5, 6, 5]
    print('List:', l)
    print('First element:', l[0])
    print('Last element:', l[-1])
    print('Length:', len(l))
    print('Max:', max(l))
    print('Min:', min(l))
    print('List using list constructor:', list(range(10)))
    print('Count 5s in l:', l.count(5))
    print('Index of 5 in l:', l.index(5))
    print('Appending 1000 at the end of list l:')
    l.append(1000)
    print(l)
    
    print('Add multiple objects at end of list.')
    l.extend(range(20))
    print(l)

    print('Insert 300 at the begining of l:')
    l.insert(0, 300)
    print(l)
    
    print('Remove 300 from l:')
    l.remove(300)
    print(l)
    
    print('Delete item at index 10 from l:')
    del l[10]
    print(l)
    
    print('Remove and return that removed value from end of the list l:')
    a = l.pop()
    print('Popped element of l:', a)
    print('l:', l)
    
    print('Pop from index 0:')
    a = l.pop(0)
    print('Popped element:',a)
    print('l:', l)
    

def func_dictionaries():
    print('Dictionaries are python version of associative arrays or hash arrays.')
    d = {'one':2, 'two': 2, 'three': 3, 'four':4,'human': 'me'}
    x = dict(animal='dog', god='almighty', hero='batman')
    print('d-> {}'.format(d))
    print('x-> {}'.format(x))
    
    print('Combine two dictionaries:')
    a = {**d, **x}
    print('Combined Dictionaries:', a)
    
    print('Check for \'four\' in a:', ('four' in a))
    print('Check for absence of \'alpha\' in a:', ('alpha' not in a))
    
    for k, v in a.items(): print(k, v, end='|')
    
    print('Use get method of dictionary to get a value for key and not the key-index because key-index with throw exception.')
    print('While get method gives \'None\'.')
    try:
        print(a['Morrow'])
    except Exception as e:
        print('Exception thrown as {}'.format(e))
        
    print('Not present shown in NONE type:', a.get('Morrow'))
    
    print('Setting different default:', a.get('Morrow', 'Not present in dictionary'))
    
    print('Popping a value from p:')
    b = a.pop('god')
    print(a)
    print('popped value ->', b)
    
def byte_n_byte_array():
    print('Bytes and Bytesarray contain bytes and not any other objects like in lists and tuples.')
    print('1byte = 8 bits')
    print('1byte = 256 different values')
    print('bytearray - mutable list of bytes.')
    print('Note: ord(\'char\') gives the integer equivalent of that character.')
    print('Normal ASCII range: 0 to 127')
    
    print('Open file sample.txt for reading(\'r\') and with encoding as utf_8 and ignore the default encoding.')
    file_in = open('sample.txt', 'r', encoding = 'utf_8')   # open input file
    
    file_out = open('sample.html', 'w')       # opening output file to write('w')
    
    outbytes = bytearray()  # initialize the byte array
    
    for line in file_in:    # iterate through the file
        for c in line:      # iterate through each character of the line
            if ord(c) > 127:    # check if the integer equivalent of the character is out of normal ascii range
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')    # append bytes to bytearray container using (+=) operator and formating as utf_8
            else: outbytes.append(ord(c))    # if character is with the normal ascii range append as it is to bytearray container
    
    outstring = str(outbytes, encoding = 'utf_8')   # output as string from bytearray
    print(outstring, file = file_out)               # print the output string to the output file file_out(sample.html)      
    print(outstring)
    
    print('Yo!!')
    
def main():
    func_tuple()
    print()
    func_list()
    print()
    func_dictionaries()
    print()
    byte_n_byte_array()

if __name__ == '__main__': main()