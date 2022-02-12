#Lab 06 - Credit Card Vaidator - Working

#ask user to input the cc number
user_cc = input("What is the credit card number? :")

#define function to validate cc number
def ccv(user_cc):
    #convert string to list of integers
    list_cc = list(map(int, user_cc))
    print(f"Initial CC number: {list_cc}")
    #store last digit as check_digit using slice
    check_digit = list_cc[-1:]
    print(f"Check digit: {check_digit}")
    #delete the last digit
    list_cc.pop(-1)
    print(f"Initial CC number, last digit deleted: {list_cc}")
    #reverse the list
    list_cc = list_cc[::-1]
    print(f"Reversed CC number: {list_cc}")
    #double every other starting with 1st
    list_cc[::2] = [2*i for i in list_cc[::2]]
    print(f"Every other cc number doubled: {list_cc}")
    #subtract nine from any number over 9
    list_cc[::2] = [i-9 if i > 9 else i for i in list_cc[::2]]
    print(f"9 subtracted from numbers over 9: {list_cc}")
    #sum all values
    sum_cc = int(sum(list_cc))
    print(f"sum of values {sum_cc}")
    #get second digit of sum
    second_dig_sum = sum_cc % 10
    print(f"Second digit of sum: {second_dig_sum}")
    #compare second digit of sum to check digit, report validity
    if second_dig_sum == check_digit[0]:
        print("\nValid")
    else:
        print("\nInvalid")

ccv(user_cc)
