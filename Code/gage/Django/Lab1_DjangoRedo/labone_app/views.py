from doctest import OutputChecker
from django.shortcuts import render, redirect, reverse
import random
# from .forms import UserAuthForm 
# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    result = request.POST['num'] # Accesses input from user
    
    user_num = int(result)
    # Collects the tens digit from the user input
    tens = user_num // 10
    # Collects the ones digit from the user input
    ones= user_num % 10

    if user_num < 100:
        # Base phrases for the tens place
        number_word_tens = ['zero','one', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'nintey']
        # Base digits for the ones place
        number_word_ones = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        # Base digits for teen values
        number_word_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

        # Checks if the user entered a single digit number
        if number_word_tens[tens] == 'zero':
            number_word_tens[tens] = ''

        # Checks if the number is in the teens 
        if tens == 1:
            output = f"The number {user_num} is {number_word_teens[ones].title()}"

        else:
            output = f"The number {user_num} is {number_word_tens[tens].title()}{number_word_ones[ones].title()}"



    # Checks if user entered a 3-digit number
    elif user_num >= 100:
        
        # Converts 3 digit number into a list in order to separate each value
        user_num = (str(user_num))
        user_num_list = []

        for numbers in user_num:
            user_num_list.append(int(numbers))

        # Separates the hundredths place from the rest if the number
        second_half = str(user_num_list[1]) + str(user_num_list[2])
        second_half = int(second_half)
        # Collects tens digit based on the list above
        tens = second_half // 10
        # Collects ones digit based on the list above
        ones = second_half % 10
        # Collects hunds digit based on the list above
        hunds = user_num_list[0]
        
        # All possible base values in english
        number_word_tens = ['zero','one', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'nintey']

        number_word_ones = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        number_word_hunds = ['zero','One Hundered', 'Two Hundred', 'Three Hundered', 'Four Hundered', 'Five Hundered', 'Six Hundered', 'Seven Hundered', 'Eight Hundered', 'Nine Hundered']

        number_word_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        # Checks if the user entered a teens digit
        if tens == 1:
            output = f"The number {user_num} is {number_word_hunds[hunds]} and {number_word_teens[ones].title()}"
        # Checks if user entered a digit between 101 and 109
        elif tens == 0 and ones != 0:
            output = f"The number {user_num} is {number_word_hunds[hunds]} and {number_word_ones[ones]}"
        # Checks if user entered 100
        elif tens == 0:
            output = f"The number {user_num} is {number_word_hunds[hunds]}"
        elif ones == 0:
        
            output = f"The number {user_num} is {number_word_hunds[hunds]} and {number_word_tens[tens].title()}" 
        else:
            output = f"The number {user_num} is {number_word_hunds[hunds]} and {number_word_tens[tens].title()} {number_word_ones[ones].title()}"
        
    print(output)
    context = {
        'output': output,
    }
    return render(request, 'result.html', {'output':output})