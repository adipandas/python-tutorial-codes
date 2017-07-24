'''
Created on Jul 24, 2017

@author: Aditya

This code is just the discussion of Python Variable basics

# everything in python is objects
# variables in python are references to objects

Variables and Types in python can be mutable(can be changed) or immutable(cannot be changed)
'''

def variable_type_id():
    
    x= 43
    print(id(x), x, type(x))
    
    x= 42
    print(id(x), x, type(x))
    
    y = 42
    print(id(y), y, type(y))
    
    print('Notice y and x have same ids for the value 42.')
    print('This the variables in python refer to objects. 42 is a int object in this case.')
    
    print()
    print('Compare values of two objects:')
    print(x==y)
    
    print('Compare IDs of two objects:')
    print(x is y)
    
    print()
    print('Mutable objects IDs')    
    x = dict(x=42)
    y = dict(x=42)
    
    print('Compare values of x and y:')
    print(x == y)
    print('Compare IDs of x and y:')
    print(x is y)
    
    print('''\
Notice that dictionary being mutable objects creats a different object for different variable names.
Thus, the different ids for x and y even though they have same values.
''')

def variable_basic_ops():
    x=42    # object is created
    print('ID of x={} is {}'.format(x, id(x)))
    
    x=43
    print('ID of x={} is {}'.format(x, id(x)))
    
    x=42    # object is created
    print('ID of x={} is {}'.format(x, id(x)))
    
    print('It can be seen that variable x is changed to refer different objects.')
    
    print('Numbers, strings and tuples in python are immutable fundamental types/objects.')
    
    print('List and Dictionaries are some of the mutable objects.')
    
    
    # Note: Python has two different kinds of numbers
    num = 42
    print(type(num), num)        # integer type
    
    num = 42.0
    print(type(num), num)       # floating type
    
    num = 42 / 9
    print(type(num), num)       # division will turn to floating type
    
    num = 42 // 9               # remainder in python
    print(type(num), num)       # returns an integer type as remainder
    
    num = round(42/9)
    print(type(num), num)       # round up the result of division
    
    num = round(42/9, 2)        # round up the result up to two decimal places
    print(type(num), num)
    
    num = 42 % 2                # remainder with modulo operator also works in python
    print(type(num), num)
    
    num = float(42)             # constructor of class 'float' - integer is converted to float
    print (type(num), num)
    
    num = int(42.8)             # constructor for class 'int' in python - float is converted to integer
    print(type(num), num)
    
    print("This is a string example.\'format\' is the method of string object")
    
    print(r"This is an example of raw\nstring")
    
    print()
    print('\'format\' example.\nnum={}'.format(num))
    
    print()
    s = '''\
Hello world, multiple lines can be inserted in python code using string objects
This is awesome in python.
I am in love with Python.
    '''
    print(s)
    
    
    print()
    print('Logical values in python:')
    a, b = 0, 1
    print (a==b)
    print(a<b)
    
    a=True
    b=False
    print(id(a))
    print(id(True))
    print(id(b))
    print(id(False))
    print('Notice both IDs are equal for a and True. They are also equal for b and False.')
    print('Logical values in python belong to the following class')
    print(type(True), True)
    print(type(False), False)


def main():
    
    variable_type_id()
    print()
    variable_basic_ops()
    
    
if __name__ == '__main__': main()