'''
Created on Jul 30, 2017

@author: Aditya

This program demonstrates the concept of the regular expressions in python.

Simple efficient regular expression in python -  using 're.compile'

'''


import re   # regular expression module in python

def simple_regex():
    fh = open('sample.txt')
    for line in fh:
        # define a regular expression and print the line which has it
        if re.search('(R|i)OS', line): print(line, end='')
        
        # to print only group of text which was matched with expression
        match = re.search('(R|i)OS', line)
        if match:
            print(match.group())
            
def search_and_replace():
    # search and replace example using regular expressions in python
    print('')
    print('Search and Replace demo:')
    fh = open('sample.txt')
    for line in fh:
        print(re.sub('(R|i)OS', '###', line), end='')
    
    print('Notice the entire file is printed.\nThus, \'re.sub\' prints the string even if the expression is not found.')
    
def search_and_replace_2():
    print('\nWork around to avoid printing entire file using search and replace.\
    \nPrint only the strings/lines where the pattern from regular expression was found:')
    
    fh = open('sample.txt')
    for line in fh:
        match = re.search('(R|i)OS', line)
        if match:
            print(line.replace(match.group(), '###'), end='')

def efficient_regex():
    print('\nTo make efficient string search with regular expression:\ndefine the pattern and compile it once at the begining and then reuse it later as per the need.')
    fh = open('sample.txt')
    pattern = re.compile('(R|i)OS')     # Precompile regular expression
    
    for line in fh:
        if re.search(pattern, line): print(line, end='')

def search_and_replace_ignore_case():
    # Compiled regular expression
    print('\nExample demonstrating ignore_case while search and replace.')
    fh = open('sample.txt')
    pattern = re.compile('(R|I)OS', re.IGNORECASE)  # Precompiled regular expression
    
    for line in fh:
        match = re.search(pattern, line)
        if match:
            print(line.replace(match.group(), '###'), end='')
            print(pattern.sub('###',line), end='')
            
def main():
    simple_regex()
    
    search_and_replace()
    
    search_and_replace_2()
    
    efficient_regex()
    
    search_and_replace_ignore_case()
    
if __name__ == '__main__':main()