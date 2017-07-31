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
    
if __name__ == '__main__': main()
