'''         +-+#^#+--+#^#+--+#^#+-+             
        Project: Credit Card Validation           ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/11/22                    ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''

def card_validator(card_num):
    """Validates user's cc number to be true or false"""
    # convert integers to a list
    card_num = list(int(i) for i in str(card_num)) # converts num back to a str so it is iterable then treats each index as a number and puts it into a list
    
    # remove last digit from list
    check_num = card_num.pop(-1)

    # Reverse all nums in list
    card_num = card_num[::-1] 

    # double every other number in list
    card_num[::2] = [2 * i for i in card_num[::2]]
        
    # Subtract 9 from numbers over 9 in list
    card_num = [i-9 if i > 9 else i for i in card_num]   
        
    # Sum all values in list
    card_num = sum(card_num)

    # Check econd digit of sum to see if it matches check digit from original number
    if int(str(card_num)[1]) == check_num:
        # Card is Valid
        return True
        
    else:
        #Card is Invalid
        return False
        


def main():
    """Credit card validator"""
    # Loop to get a "valid" number before being checked by validator
    while True:
           
            try:
                user_card = int(input("Enter Card Number\n")) # ensures input is a valid number
                if len(str(user_card)) == 16: 
                    print("Thank you")   
                   
                    # If card is valid, True, print card is valid
                    if card_validator(user_card) == True:
                        print("Thanks your card is Valid")
                        continue
                    
                    # If card is invalid, False, print card is invalid
                    elif card_validator(user_card) == False:
                        print("Your card is invalid")
                        continue   
                else:
                    print("Enter valid card number")    

                
            except ValueError: 
                print("Invalid Entry\n")



if __name__ == "__main__":
    main()
