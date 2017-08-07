'''
Created on Aug 6, 2017

@author: Aditya

'''

class GOT:
    def __init__(self, **kargs):
        self.properties = kargs

    def what(self):
        print('GOT is Game of Thrones!!')
    
    def purpose(self):
        print('GOT tells the story of 7 kingdoms and the ruler of those kingdoms.')
        
    def get_properties(self):
        return self.properties
    
    def get_property(self, key):
        return self.properties.get(key, None)
    
    @property
    def kingdom_animal(self):
        return self.properties.get('kingdom_animal', None)
    
    @kingdom_animal.setter
    def kingdom_animal(self, a):
        self.properties['kingdom_animal'] = a
        
    @kingdom_animal.deleter
    def kingdom_animal(self):
        del self.properties['kingdom_animal']

def main():
    print('''Decorators in python are used to create accessor methods for variables.''')
    houseStark = GOT(kingdom_animal = 'Wolf', location = 'North')
    print(houseStark.get_properties())
    print(houseStark.get_property('kingdom_animal'))
    print(houseStark.get_property('location'))
    
    print('\nDemo of Decorators:')
    print('Getter:', houseStark.kingdom_animal)
    
    del houseStark.kingdom_animal
    
    print(houseStark.kingdom_animal)
    
    houseStark.kingdom_animal = 'Lion'
    print(houseStark.kingdom_animal)
    

if __name__ == '__main__': main()