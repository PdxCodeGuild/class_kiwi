#built in funcations
#print()
#input()
#type()
#round()

"""
# Anatomy of a funcation
def funcation_name(parameters):
    '''docstring'''
    statement1
    statement2
    ...
    ...
    return [expression]
"""


def greet(first_name = "", last_name = ""):
    '''
    Print a welcome message to the console
    '''
    print(f"Hello {first_name} {last_name}")

# greet("Barry", "Allen")
# greet('Harry')
# greet()

# greet(last_name="Ross", first_name="Bob")



def subtract(num1, num2):
    result = num1 - num2
    return result

sum=subtract(9, 5)
print(sum)
