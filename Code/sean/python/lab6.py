
# input for card numbers
card = input(f"Type in your credit card numbers here: ")


# function to verify if card is valid or not
def credit_card_validator(card):
    card = list(card)           
    card_int = []
    card_reversed = []       #I use these 3 empty lists later to append to once I have looped and chaged each list item
    card_9 = []

    for i in card:                 #changing list to int, appending to new list
        card_int.append(int(i))
    
    check_digit_1 = card_int.pop()    #taking last digit out and saving it

    for i in card_int[::-1]:        #looping through reversed list with slicing then appending to new list in reversed order
        card_reversed.append(i)

    counter = 0                     #counter is to keep track of index at every step so i can add the item back to list
    for i in card_reversed[0::2]:   #slicing stars at index 0 and does steps of 2 to the end of list
        num = (i * 2)                  #multiplying item times 2
        card_reversed[counter] = num   #re adding my mulitiplyed item back into the list at its correct index, which should be "counter"
        counter += 2                   #im adding 2 to counter because every step is 2 indexs in the list
    
    for i in card_reversed:         #subtracting 9 from items over 9
        if i > 9:                   #if item is greater than 9, subtract 9 and append to new list
            new_i = i - 9
            card_9.append(new_i)
        else:                       #if it isnt greater then just add to new list 
            card_9.append(i)

    card_sum = 0                    #adding all items together for sum
    for i in card_9:
        card_sum += i

    card_str = str(card_sum)            
    check_digit_2 = card_str[1]         #changing to string and taking out last digit then changing back to int
    check_digit_2 = int(check_digit_2)


    if check_digit_1 == check_digit_2:
        return True
    else:
        return False
    
    
    

valid = credit_card_validator(card)

if valid == True:
    print("Your credit card is valid.")

elif valid == False:
    print("Your credit card is Invalid.")