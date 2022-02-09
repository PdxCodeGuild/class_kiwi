

number = int(input("Please provide a number: "))

# extraction of ones and tens digits
tens_digit = number//10
ones_digit = number % 10

ones_list = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]

teens_list = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens_list = ["", "", "twenty", "thirty", "fourty", "fifty",
             "sixty", "seventy", "eighty", "ninety"]

hundreds_list = ["one hundred", "two hundred", "three hundred", "four hundred",
                 "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]

if number < 10:
    value = ones_list[number]
    print(value)
elif 10 < number < 20:
    value = teens_list[ones_digit]
    print(value)
elif number > 19:
    value = tens_list[tens_digit], ones_list[ones_digit]
    print(value)
