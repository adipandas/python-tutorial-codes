'''
Created on Jul 23, 2017

@author: Aditya

# This example shows the MVC pattern in OOP for Python
MVC - Model View Controller
OOP - Object oriented programming
'''

# --- VIEW ---
class AnimalActions:
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')
    
    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}.'.format(self.animalName(), action)
        
    def animalName(self):
        return self.__class__.__name__.lower()

# ---- MODEL ----
class Duck(AnimalActions):      # class Duck inherits class AnimalActions
    strings = dict(
        quack = 'Quack!',
        feathers = 'Duck has feathers.'
        )

class Dog(AnimalActions):      # class Dog inherits class AnimalActions
    strings = dict(
        bark = 'Bow bow!',
        fur = 'Dog has blue fur.'
        )
class Person(AnimalActions):      # class Person inherits class AnimalActions
    strings = dict(
        bark = 'Person makes a dog sound.',
        fur = 'Person has some soft fur coat.',
        quack = 'Person makes quacking sound.',
        feathers = 'Person has some bird feathers.'
        )
    
# ---- CONTROLLER ----

def in_doghouse(dog):
    print(dog.bark())
    print(dog.fur())
    
def in_jungle(duck):
    print(duck.quack())
    print(duck.feathers())
    
def main():
    donald = Duck()
    john = Person()
    doggy = Dog()
    
    print("-- In the JUNGLE:")
    for o in (donald, john, doggy):
        in_jungle(o)
        
    print("-- In the Dog-House")
    for o in (donald, john, doggy):
        in_doghouse(o)
        
    
if __name__ == '__main__': main()
