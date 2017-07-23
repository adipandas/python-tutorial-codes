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
        

if __name__ == '__main__':
    for n in range(1, 20):
        isprime(n)