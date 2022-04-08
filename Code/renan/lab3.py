

from argparse import ONE_OR_MORE


def get_number():
    '''Convert Numbers To Phrase'''
    
    num = int(input("What Number: "))  
    
    one_dict= {
        0: " ",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Tweleve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",  
    }     
    ten_dict= {
        0: " ",
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
    
  
    tens_digit = num // 10 #If using 143 = 14
    teens_digit = num % 100
    ones_digit = num % 10 # IF using 143 = 3 = one_dict[3]
    hnds_digit = num // 100 #if using 143 =  one_dict[1]
    
    alternative = tens_digit % 10
    # print(alternative, "alternative test")
    
    if num in range(0, 20):
         print(one_dict[num])
    
    elif 20 < (num) <= 99:
         print(ten_dict[tens_digit] +" " + one_dict[ones_digit]) 
         
    elif 11 <= (teens_digit) <= 19:
        print(one_dict[hnds_digit] + " hundred " + one_dict[teens_digit])
    
    elif 100 < (num) <= 999:
         print(one_dict[hnds_digit] + " hundred " + " " + ten_dict[alternative] + " " + one_dict[ones_digit])
         
       
    
get_number()


    


