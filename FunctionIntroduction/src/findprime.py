'''
Created on Jul 22, 2017

@author: Aditya

This code defines a simple function
to check if the given number is prime or not
'''

def isprime(n):
    if n ==1:
        print("1 is special")
        return False
    for i in range(2,n):
        if n%i == 0:
            print('{} equals {} x {}.'.format(n, i, n//i))
            return False
    else:
        print(n, 'is a prime number.')
        
def optional_arg_func(a, b=None, c=30):
    print('This demonstrates optional arguments for the functions.')
    print('since b and c have default values in the function arguments, these are optional.\nFunction call will woork even if b and c are not provided.')
    print('\'a\' has no default. Therefore, it becomes a mandatory argument for the function.')
    print('Value of b is None.\nNone is given as a variable value when variable is to be kept as optional in function arguments but one does not want to assign any value to it.')
    print('Default arguments cannot be defined before non-default arguments.')
    
    if b is None:
        b = 433
    
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('c={}'.format(c))

def arbitrary_list_arg_func_1(*args):
    print('*args: stands for list of optional arguments')
    print('Notice arbitrary arguments are passed as a tuple to the function. Thus, one can use it as a iterator.')
    print(args)

def arbitrary_list_arg_func_2(a, b, c, *args):
    print('*args: stands for list of optional arguments')
    print(a, b, c, args)
    
def key_word_func_args(a, b, *args, **kargs):
    print('Key word function arguments are discussed in this function')
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('arbitraty number of arguments as tuple = {}'.format(args))
    print('\nFollowing represents key-word arguments:')
    print('NOTE: key-word arguments are actually passed as dictionary to the function.')
    
    for k in kargs:
        print('key = {} and value = {}'.format(k, kargs[k]))
        
def func_return_multiple_val():
    print('Demo of returning multiple values in python')
    a = 1
    b = 2
    c = 3
    d = 'This is a string'
    return a, b, c, d

def generator_func_demo():
    print('This function is a demo of generator function.')
    print('Generator function returns an iterator object.')
    
    print('The function used here, is a generator function for inclusive range.')
    for i in inclusive_range(0,10,1):
        print(i, end=' ')

def inclusive_range(*args):
    n_args = len(args)
    if n_args < 1: raise TypeError('Minimum 1 argument required.')
    
    if n_args == 1:
        start = 0
        step = 0
        stop = args[0]
    elif n_args == 2:
        (start, stop) = args
        step = 1
    elif n_args == 3:
        (start, stop, step) = args
    else: raise TypeError('Maximum 3 arguments required. Given {} arguments to the function'.format(n_args))
    
    i = start
    while i<=stop:
        yield i             # yield makes the function as a generator function
        i += step
    
def main():
    for n in range(1, 20):
        isprime(n)
    
    print()
    optional_arg_func(n)            # do not provide optional arguments
    print()
    optional_arg_func(n, 30, 50)    # give optional arguments
    print()
    arbitrary_list_arg_func_1(1,2,3,4,5)
    print()
    arbitrary_list_arg_func_2(1, 2, 3, 4,5,6,7)
    print()
    key_word_func_args(3, 45, 1 , 2, 3, one = 1, two = 2, three = 3)
    print()
    
    a, b, c, d = func_return_multiple_val()
    print('a={}, b = {}, c={}\nd={}'.format(a,b,c,d))
    
    print()
    generator_func_demo()
        
if __name__ == '__main__': main()
