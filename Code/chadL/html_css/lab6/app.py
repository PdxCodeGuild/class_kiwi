from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    #name = "chad"
    return render_template('index.html')

if __name__ == "__main__":
  app.run()

#  $env:FLASK_APP = "app.py"
#   $env:FLASK_ENV = "development"

#Lab 7: ROT Cipher

hacker = input("What shall we encypt? ").lower()       #ask user for words to encypt

rot13_dict = {                                          #dictinary of associated letters
    "a": "n",
    "b": "o",
    "c": "p",
    "d": "q",
    "e": "r",
    "f": "s",
    "g": "t",
    "h": "u",
    "i": "v",
    "j": "w",
    "k": "x",
    "l": "y",
    "m": "z",
    "n": "a",
    "o": "b",
    "p": "c",
    "q": "d",
    "r": "e",
    "s": "f",
    "t": "g",
    "u": "h",
    "v": "i",
    "w": "j",
    "x": "k",
    "y": "l",
    "z": "m", 
    " ": " "   
}

hacker = list(hacker)                                   #turn input into list


def rot_13(hacker):                                     #fucntion to turn input into list.
    rot13_list = []
    for letter in hacker:                               #loop to add appended letter to list
        cypher = rot13_dict[letter]                     
        rot13_list.append(cypher)                       # add cypher to rot13 list
    
    final_answer = ''.join(rot13_list)                  # .join seperates everything except the letters.
    print(f"Your encrypted code is:  {final_answer}")                
       
rot_13(hacker)