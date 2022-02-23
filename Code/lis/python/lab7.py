# Lab 7 ROT Cipher

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotation = 13


# create function
def cipher(user_input): 
  ciphered_text = ""
  user_input = user_input.upper()

  for x in user_input:
    ciphered_text += (letters[(letters.index(x) + rotation) % 26])
  
  return(f"the ciphered code for {user_input} is: {ciphered_text}")
  

# get input
while True:
    user_input = input("Enter text to cipher using ROT13 or 'done' to quit: ")
    if user_input == 'done':
        break
    
    if user_input.isalpha():
      # call function
      print(cipher(user_input))  
    else:
      print("Enter characters A-Z only")
    
    