# built in functions
# print()
# input()
# type()
# round()

"""
# anatomy of a function
def function_name(parameters):
    '''docstring'''
    statement1
    statement2
    '''
    '''
    return [expression]
"""

def greet(first_name, last_name=""):
    '''
    print a welcome message to the console
    '''
    print(f'hello {first_name} {last_name}')


greet('Barry', 'harry')
greet(' ')
greet('Ron', 'Barry')

def subtract(num1, num2):
    result = num1 - num2
    return result

subtract(7, 5)