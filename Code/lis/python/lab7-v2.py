# Lab 7 version 2  ROT Cipher

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# create function
def cipher(rotation, user_input): 
  ciphered_text = ""
  user_input = user_input.upper()

  for x in user_input:
    ciphered_text += (letters[(letters.index(x) + rotation) % 26])
  
  return(f"the ciphered code {user_input} using ROT{rotation} is: {ciphered_text}")
  

# get input
while True:
    rotation = int(input("Enter the cipher rotation number: "))
    user_input = input("Enter text to cipher or 'done' to quit: ")
    if user_input == 'done':
        break
    
    if user_input.isalpha():
      # call function
      print(cipher(rotation, user_input))  
    else:
      print("Enter characters A-Z only")
    

    
    