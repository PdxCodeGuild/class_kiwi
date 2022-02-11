

from argparse import ONE_OR_MORE


def get_number():
    '''Convert Numbers To Phrase'''
    
    num = int(input("What Number: "))
    
    
    
    
    one_dict= {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        
        
    }

    ten_dict= {
        1: "One",
        2: "Twenty",
        3: "Thrity",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seveny",
        8: "Eighty",
        9: "Ninety",
        
        
    }

    tens_digit = num // 10
    ones_digit = num % 10
    
    if (num) <= 9:
         print(one_dict[ones_digit])
         
    elif (num) >= 20:
        print(ten_dict[tens_digit] +" " + one_dict[ones_digit]) 
    
get_number()



    


