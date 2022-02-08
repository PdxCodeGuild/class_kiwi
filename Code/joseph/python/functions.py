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

# create function that says the temperature in english
def get_temperature(temp: float) -> str:
    '''function takes in temp as number returns temp in english'''

    if temp > 90:
        return "Hot"
    elif temp >75 and temp <=90:
        return "Warm"
    elif 60 < temp <=75:
        return "Comfortable"
    elif 45 < temp <=60:
        return "Chilly"
    elif temp <= 45:
        return "Freezing"