# Built in functions
# print()
# input()
# type()
# round()

"""
# Anatomy of a function
def function_name(parameters):
    '''docstring'''
    statement1
    statement2
    ...
    ...
    return [expression]
"""


from webbrowser import get


def greet(first_name, last_name = ""):
    '''
    Print a welcome message to the console.
    '''
    print(f"Hello {first_name} {last_name}")

def phone_book(last_name, first_name=""):
    pass


# greet("Barry", "Allen")
# greet("Harry")
# greet()

# greet("Bob", last_name="Ross")


def subtract(num1, num2):
    result = num1 - num2

    return result


# Create a function the says the temperature in english
def get_temperature(temp: float) -> str:
    '''Function takes in temperature as number returns temperate in english'''

    if temp > 90:
        return "Hot"
    elif temp > 75 and temp <= 90:
        return "Warm"
    elif 60 < temp <= 75:
        return "Comfortable"
    elif 45 < temp <= 60:
        return "Chilly"
    elif 32 < temp <= 45:
        return "Cold"
    else:
        return "Freezing"


# print(get_temperature(80))

# temp = get_temperature(40)
# print(temp)




def main():
    sum = subtract(12, 2)

    counter = 0
    # while counter < sum:
    #     counter += 1
    #     greet("Joe", counter)


# main()

if __name__ == "__main__":
    main()

# print(__name__) # = __main__ if running file directly, name of module if imported