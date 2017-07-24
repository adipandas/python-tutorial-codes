'''
Created on Jul 24, 2017

@author: Aditya
This code is example for Tuples, Lists, Strings and Dictionaries in python
'''

def list_tuples_string():
    print("Defining Tuple in python: (remember that tuple is immutable object)")
    x = (1, 2, 3)
    print(type(x), x)
    print()
    
    print('Defining Lists in python: (Lists are mutable)')
    x = [1, 2, 3]
    print(type(x), x)
    print()
    
    print('Changing the List:')
    x.append(5)     # appending the element at the end of list
    print(x)
    print()
    
    print("Inserting the element in the list: list_name.insert(index, value)")
    x.insert(3,7)
    print(x)
    print()
    
    print("Exploring strings in python: String is immutable sequence in python")
    x= 'string'
    print(type(x), x)
    print('Slice syntax: x[inclusive_lover_limit:exclusive_upper_limit]')
    print('Example of slices of string', x[2:4])
    print()


def variable_dictionaries():
    print("Define dictionary:")
    d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5 }
    print('Example Dictionary:', d)
    
    print('If \'k\' is the key, than the value of element in dictionary \'d\' is given by d[k].')
    for k in d:
        print(k, d[k])
    
    print()
    print('To get python dictionary in sorted order:')
    for k in sorted(d.keys()):
        print(k, d[k])
        
    print('Notice keys sorted in alphabetical order')
    
    # dictionary using key-word argument
    c = dict(
        one = 1,
        two = 2,
        three = 3,
        myName = 'Aditya'
        )
    print(c)
    
    print('Add value to dictionary:')
    c['skycolor'] = 'blue'
    print(c)

def main():
    list_tuples_string()
    variable_dictionaries()
    
if __name__ == '__main__': main()