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
            
class Mouth:
    def __init__(self):
        print('Constructor is called while object is defined.')
    def speak(self):
        print('Mouth can speak.')
    def sing(self):
        print('Mouth can sing.')    
            
class Man_from_moon():
    def __init__(self, **kargs):
        print('This class defines the scalability of the class data.')
        print('Use of dictoionaries in class variable definition can make the class data scalable easily.')
        print('Dictionaries used as kwargs OR key-word arguments.')
        self.variables = kargs
        
    def get_face(self):
        print('Getting the face of man from moon')
        print('This makes it with limited scalability')
        return self.variables.get('face', None)     # default value returned for face is None
    
    def set_face(self, face):
        print('Setting the face of man from moon')
        print('This makes it with limited scalability')
        self.variables['face'] = face
    
    def get_variable(self, k):
        # k is the name of the varible
        print('using the key word variables to set and get makes it easier to deal with scalibility of class data')
        return self.variables.get(k, None)      # default value of 'None' is returned if variable not defined
    
    def set_variable(self, k, v):
        print('Key-value argument makes the class model easily scalable in python.')
        self.variables[k] = v

class Phone:
    def __init__(self):
        print('parent class')
    
    def buttons(self):
        print('Has buttons to dial a number.')
        
    def screen(self):
        print('Phone has a black and white display!')
            
class Mobile_phone(Phone):
    def __init__(self):
        print('Child class of Phone')
        
    def internet_connection(self):
        print('Can connect to internet using WiFi!')
        
    def buttons(self):
        print('Buttons on touch screen! -> Overriding buttons from Parent class Phones!')

    def screen(self):
        super().screen()   # method to access parent class methods
        print('Display is colored as a whole.')
    
class Rose:
    def color(self):
        print('Rose is Red.')
    def smell(self):
        print('Rose has a sweet smell.')
    def stem(self):
        print('Stem of rose have thorns.')
    def location(self):
        print('Rose in the garden.') 

class Lotus:
    def color(self):
        print('Lotus is pink.')
    def smell(self):
        print('Lotus has no smell.')
    def stem(self):
        print('Stem of lotus has no thorns.')
    def location(self):
        print('Lotus in the pond.')
        
def what_location_n_color(lotus):
    lotus.location()
    lotus.color()

def smell_the_flower(rose):
    rose.smell()
    
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
    
    # class data scalability discussed and demonstrated
    marty = Man_from_moon(face = 'MoonFace', intelligence = 'HighIntell')
    print('Getting face value from constructor: ', marty.get_face())    
    marty.set_face('ManFace')
    print('Getting face value from Getter Method: ', marty.get_face())
    print('\nAddressing Scalability:') 
    print('Getting value of \'face\' constructor:', marty.get_variable('face'))
    print('Getting value of \'intelligence\' set in constructor:', marty.get_variable('intelligence'))
    marty.set_variable('intelligence', 'VeryHighIntell')
    print('Getting new value of \'intelligence\':', marty.get_variable('intelligence'))
    
    print()
    print('Explaining Inheritance in Python OOP:')
    telepone = Phone()
    print('Methods of obj telephone:')
    telepone.buttons()
    telepone.screen()
    samsung = Mobile_phone()
    print('Methods of derived class:')
    samsung.internet_connection()
    samsung.buttons()
    samsung.screen()
    
    print()
    print('Explaining POLYMORPHISM in python:')
    print('Python being loosely typed language, polymorphism is inherent in this language.')
    redrose = Rose()
    redlotus = Lotus()
    for o in (redrose, redlotus):
        what_location_n_color(o)
        smell_the_flower(o)
        o.color()
    
    print('Notice how completely different objects like of class Rose and Lotus can be used in same way.\nThis is polymorphism.')
    
if __name__ == '__main__': main()