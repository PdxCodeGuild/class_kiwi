#Lab07 - ROT13 - Version 1 - Working

#Declare alphabet list with upper and lower case
alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

#define ROT13 function to take in phrase p
def rot13(p):
    #iterate through phrase p for each letter find l in alpha, add 26,
    #and join the new letter to a blank string, which is returned after
    #iteration is complete.  Use modulus to ensure 'wrap around' is achieved.
    #26 is used to account for upper and lower case without limiting or
    #converting input 
    return "".join([alpha[(alpha.find(l) + 26) % 52] for l in p])

#prompt user for phrase to encode/decode
p = input("What is the phrase to be encoded/decoded?: ")

#Call function rot13 and pass phrase p to encode, then call rot13
#and pass the rot13 of P as phrase to decode, print the results

print(rot13(p), rot13(rot13(p)))
