'''
Created on Jul 23, 2017

@author: Aditya

This code explains Inheritance and Polymorphism in Python
This example explains data abstraction

'''

# Parent Class
class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']
    
class Duck(AnimalActions):   # class Duck inherites AnimalActions
    strings = dict(
        quack = "Quack!",
        feathers = "Duck has feathers",
        bark = "Duck cannot bark.",
        fur = "Duck has no fur."
        )

class Person(AnimalActions):    # class Person inherites AnimalActions
    strings = dict(
        # object of Person class implements feathers and quack method: 
        # This is polymorphism
        quack = "Person says quack.",
        feathers = "Person has a peacock feather in the pocket.",
        bark = "Person can make barking sound.",
        fur = "Person has a fur coat."
        )
    
class Dog(AnimalActions):   # class Dog inherits class AnimalActions
    strings = dict(
        quack = "Dog cannot quack!",
        feathers = "Dog has no feathers and thus cannot fly.",
        bark ="Bow bow!",
        fur = "It has a soft white fur."
        )
    
def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())
    
def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
    

def main():
    donald = Duck()
    john = Person()
    doggy = Dog()
    
    print("- In the forest:")
    for o in (donald, john, doggy):
        in_the_forest(o)
    
    print("- In the doghouse:")
    for o in (donald, john, doggy):
        in_the_doghouse(o)
    
if __name__ == '__main__':
    main()