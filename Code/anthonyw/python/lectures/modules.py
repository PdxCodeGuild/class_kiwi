from functions import subtract, greet, get_temperature
from random import choice, randint # random.py

# import functions

def calculate_purpose_of_life():
    pass


def main():
    sum = subtract(112, 56)

    greet("Carl", "Swanson")

    temp = float(input("Enter the outside temperature: "))
    print(get_temperature(temp))


if __name__ == "__main__":
    main()