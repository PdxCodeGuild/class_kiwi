from crypt import methods
from email import message
from flask import Flask, render_template, request

app = Flask(__name__)


def rot_cipher_encrypt(message: str, shift: int):
    encrypt_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
        'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
        's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26,
    }
    decrypt_dict = {
        0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f',
        7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
        14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
        21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
    }
    encrypted_text = ''
    for letter in message:
        if letter == ' ':
            encrypted_text += letter
        else:
            num = encrypt_dict[letter]
            num = ((num + shift) % 26)
            encrypted_text += decrypt_dict[num]
    return encrypted_text


def rot_cipher_decrypt(message: str, shift: int):
    encrypt_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
        'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
        's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26,
    }
    decrypt_dict = {
        0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f',
        7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
        14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
        21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
    }
    decrypt_text = ''
    for letter in message:
        if letter == ' ':
            decrypt_text += letter
        else:
            num = encrypt_dict[letter]
            num = ((num - shift) % 26)
            decrypt_text += decrypt_dict[num]
    return decrypt_text

# message = ''
# encrypted_message = ''
# shift = 13


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():

    shift = int(request.form['shift'])
    message = request.form['user_string'].lower()
    encrypted_message = rot_cipher_encrypt(message, shift)

    # print(message)

    return render_template('encrypted.html', encrypted_message=encrypted_message, shift=shift)


@app.route('/decrypt', methods=['POST'])
def decrypt():
    shift = int(request.form['shift'])
    message = request.form['decrypt_message'].lower()
    decrypt_string = rot_cipher_decrypt(message, shift)

    return render_template('decrypt.html', decrypt_string=decrypt_string,  shift=shift)
