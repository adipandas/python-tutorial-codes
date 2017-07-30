'''
Created on Jul 29, 2017

@author: Aditya

This program demonstartes various operators and their controls in python language.
Operators covered: arithematic, bitwise, boolean, slices

Demonstration of 'range' is also available

Operator Precedence:
Boolean operators evaluated from LEFT to RIGHT

Comparison operators evaluated from RIGHT to LEFT
'''

def simple_arithematic_operators():
    print('Usage of simple arithematic operator in python.')
    
    a, b = 5, 3
    print('a = {}, b ={}'.format(a, b))
    
    print('Addition of a and b: a+b:', a+b)
    print('Subtraction of b from a: a-b:', a-b)
    print('Multiplication of a and b: a*b:', a*b)
    print('Division of a by b: a/b: ', a/b)
    print('Floor division or integer division: a//b:', a//b)
    print('Remainder of division: a % b :', a % b)
    print('Integer division and Remainder as a tuple: divmod(a,b):', divmod(a,b))
    
    print()
    num = 5
    print('num ={}'.format(num))
    num+=1
    print('Increment Operator: num+=1:', num)
    num-=1
    print('Decrement Operator: num-=1:', num)
    num*=num
    print('Multiplier operator: num*=num:', num)
    num //= 5
    print('Floor dividing operator: num //= 5:', num)
    num *= num
    num /= 5
    print('Float dividing operator: num /= 5:', num)

def bitwise_operations():    
    num=5
    print('num = {}'.format(num))
    print('binary value of num = ', end = '')
    binary_value(num)
    
    x, y = 0x55, 0xaa
    print('x={}'.format(x))
    print('Binary x=',end='')
    binary_value(x)
    
    print('\ny={}'.format(y))
    print('Binary y=', end='')
    binary_value(y)
    
    print('\nBitwise OR of x and y: ', end='')
    binary_value(x|y)
    
    print('\nBitwise AND of x and y: ', end='')
    binary_value(x & y)
    
    print('\nExclusiveOR of x and 1: ', end='')
    binary_value(x ^ 1)
    
    print('\nExclusiveOR of x and 0: ', end='')
    binary_value(x ^ 0)
    
    print('\nExclusiveOR of x and y: ', end='')
    binary_value(x ^ y)
    
    print('\nAll the bits are ON: 0xff = ', 0xff)
    print('ExclusiveOR of x and 0xff: ', end='')
    binary_value(x ^ 0xff)
    
    print('\nShift operator- Left: x << 4:', end = '')
    binary_value(x << 4)
    
    print('\nShift operator- Right: x >> 4:', end = '')
    binary_value(x>>4)
    
    print('\nUnary Operator: ~x:', end='')
    binary_value(~x)
    print()
    
# printing binary value of a number
def binary_value(n):
    print('{:08b}'.format(n))   # {:08b} prints binary value to 8 places

def boolean_operators():
    print('Function demonstrating boolean operators:')
    a, b = True, False
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('a and b =',(a and b))
    print('a or b =',(a or b))
    print('a and a =', (a and a))
    print('b and b =', (b and b))
    
    
def slices_operator():
    l = [2, 3, 4, 5, 41, 52, 9, 4, 8, 9] # define a list
    
    print("Note: Python list are index \'zero\' based.")
    print('List l ={}'.format(l))
    print('0 through 5 items in the list l = l[0:5]= {}'.format(l[0:5]))
    print('2 through 6 items in list l = l[2:6]= {}'.format(l[2:6]))
    print('l[a:b] - Notice that \'a\' inclusive and \'b\' exclusive.')
    
    print("""\nRemember: Ranges in Python are non-inclusive.
These ranges never include the last item.""")
    
    
    # Use of range function    
    lst = [i for i in range(100)]
    print('lst=', lst)
    
    # Shortcut for the above list formation
    lst[:] = range(100)
    print('lst=', lst)
    
    
    print('lst[27:43] = {}'.format(lst[27:43]))
    print('lst[27:42] = {}'.format(lst[27:42]))
    print('lst[27:42:3] = {}'.format(lst[27:42:3]))
    print('lst[27:43:3] = {}'.format(lst[27:43:3]))
    
    print()
    print('Demonstrating Assignment using slicing:')
    lst[27:43:3] = (99,99,99,99,99,99)
    print(lst)
    
    print('Partial slicing of list')
    
    print('lst from 60th element to the end = {}'.format(lst[60:]))

def main():
    simple_arithematic_operators()
    print()
    
    bitwise_operations()
    
    boolean_operators()
    print()
    
    slices_operator()
    

if __name__ == '__main__':main()