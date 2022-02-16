#Lab07 - ROT13 - Version 2 - Working

#Declare alphabet list with upper and lower case
alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

#define rotX function
def rotX(x:int, p:str):
    #iterate through phrase p for each letter find l in alpha, add x*2,
    #and join the new letter to a blank string, which is stored as enc.
    #Use modulus to ensure 'wrap around' is achieved.
    #x*2 is used to account for upper and lower case without limiting or
    #converting input
    enc = "".join([alpha[(alpha.find(l) + x * 2) % 52] for l in p])
    #decode the phrase by performing nearly the same line on the variable
    #enc, but subtracting x*2 from l in alpha
    dec = "".join([alpha[(alpha.find(l) - x * 2) % 52] for l in enc])
    #return enc and dec
    return enc, dec

#ask user for the string to be encoded/decoded
p = input("What is the string to be encoded and decoded?: ")
#Ask user for the amount of rotations
x = int(input("How many rotations would you like to use for encrypting/decrypting?: "))
#Call the rotX function passing rotations as the first variable and phrase as second
#and print the output to the terminal
print(rotX(x, p))