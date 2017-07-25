'''
Created on Jul 25, 2017

@author: Aditya

This program explains various conditionals in python
'''

def if_cond():
    print('Example of \'if\' condition')
    
    a,b=0,1
    if a<b:
        print('a({}) is less than b({})'.format(a, b))
   
def if_else_cond():
    print('Example explaining \'if-else\' conditioning:')
    a,b=1,0
    if a<b:
        print('a({}) is less than b({})'.format(a, b))
    else:
        print('a({}) is not than b({})'.format(a, b))
        
def elseif_cond():
    print('Example explaining if-else cascading')
    a, b = 1,1
    if a<b:
        print('a({}) is less than b({})'.format(a, b))
    elif a>b:
        print('a({}) is greater than b({})'.format(a, b))
    else:
        print('a({}) is equal to b({})'.format(a, b))
        
def switch_cond():
    print('Example for switch control structure in python')
    
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third'
        )
    v = 'one'
    default = 'The choice does not exists.'
    print(choices.get(v, default))
    
    print(choices.get('seven', default))
    
    
def cond_expression():
    a, b = 1, 1
    v = 'a({}) is greater than b({})'.format(a, b) if a<b else 'a({}) is not greater than b({})'.format(a, b)
    print(v)

def main():
    print('This program explains conditionals in python')
    print()
    if_cond()
    print()
    if_else_cond()
    print()
    elseif_cond()
    print()
    switch_cond()
    print()
    cond_expression()
    print()


if __name__ == '__main__':main()