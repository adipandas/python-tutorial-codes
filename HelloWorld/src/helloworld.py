'''
Created on Jun 15, 2017

@author: adicds
'''
# function definition
def isprime(n):
    if n ==1:
        print('1 is special')
        return False
    
    for x in range(2, n):
        if n%x==0:
            print("{} equals {}x{}".format(n,x, n//x))
            return False
        else:
            print(n, "is a prime number")
            return True


            
if __name__ == '__main__':
    print("Hello, World!")
    
    # Declaring values in python
    a, b = 0, 1
    
    # To find the type of variable in python
    print('Variable type of \'a\' is', type(a))
    
    # This is a conditionals example: CONDITIONAL EXECUTION    
    if a<b:
        print('a({}) is less than b({})'.format(a, b))
    elif a>b:
        print('a({}) is greater than b({})'.format(a, b))
    else:
        print('a({}) is equal to b({})'.format(a, b))
    
    
    # Conditional expressions OR Conditional Value
    print("a-foo" if a < b else 'a-bar')
    
    # while loop example with Fibonacci series
    c, d = 0, 1
    while b<50:
        print(b)
        a,b = b, a + b
    
    print('End of While')
    
    print('')
    # For loop example
    """
    For loop works with iterators.
    Iterator is an object that each time you call it, 
    it gives you the next value 
    """
    # Read lines from the file using for loop
    fh = open("../lines.txt")
    for line in fh.readlines():
        print(line, end='')
        
    print("End of For")
    
    # using functions
    for n in range(1,20):
        isprime(n)
    

    
    

    