'''
Created on Jun 16, 2017

@author: adicds
'''

# generator function creates an iterator
# keyword for generator function: yield


# utility function to check prime number

def isprime(n):
    if n==1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


"""
# Generator function block:
    # One must notice that because of 'yield', 
    # the function returns the value of n
    # After this return if the function is called again,
    it continues from the next value of n.
    # Thus, it can be observed that ITERATOR is created because of generator function
"""
def primes(n=1):
    while(True):
        
        if isprime(n): yield n
        n += 1
    

if __name__ == '__main__':
    for n in primes():
        if n > 100: break
        print(n)

#NOTE: utility function is a piece of computer software designed for a routine task, such as examining or copying files
# Notice that this code uses for-else loop in python