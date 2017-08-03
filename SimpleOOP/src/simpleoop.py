'''
Created on Jul 23, 2017

@author: Aditya

This program introduces simple OOP program in python using Fibonacci Series
'''


# Note: Class is a blue print or template
#        Object is an instance of a Class

# Fibonacci series: Sum of two numbers defines a next number


# Class definition
class Fibonacci:
    # constructor of the class
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # method in the class
    def series(self):
        while(True):
            yield self.b
            self.a, self.b = self.b, self.a+self.b
            
class Mouth():
    def __init__(self):
        print('Constructor is called while object is defined.')
    def speak(self):
        print('Mouth can speak.')
    def sing(self):
        print('Mouth can sing.')    
            
def main():
    # instantiate: make object of the class
    f = Fibonacci(0,1)
    for r in f.series():            # since the method is generator function, use it as iterator
        if r>100: break
        print(r, end=' ')           # Print the Fibonacci series separated by a line
    print()
    
    # Simple class defined as Mouth
    my_mouth = Mouth()      # my_mouth = object of the class Mouth
    my_mouth.speak()
    my_mouth.sing()

if __name__ == '__main__': main()
