from flask import Flask, render_template, request
# this creates a python based webserver
app = Flask(__name__)

def encrypt(text):
    # text = input("Please enter in a string: ").lower().replace(" ", "")
    cipher = []
    for i in range(len(text)):
        char = text[i]
        encrypt = ord(char) + 13
        if encrypt < 123:
            encrypt = chr(encrypt)
            cipher.append(encrypt)
            # print(cipher)
        elif encrypt >= 122:
            repeat = (encrypt % 122) + 96
            repeat = chr(repeat)
            cipher.append(repeat)
            # print(cipher)
    return cipher

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ROT_cipher', methods=['POST'])
def ROT_cipher():
    user = request.form['user']
    user1 = user.lower().replace(" ", "")
    word = encrypt(user1)
    return render_template('ROT_cipher.html', user1=user1, user=user, word=word)