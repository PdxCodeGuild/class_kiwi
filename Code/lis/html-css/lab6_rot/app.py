from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cipher', methods=['POST'])
def cipher():
    result = request.form

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphered_results = ""
    cipher_original = result['cipher'].upper()
    rotation = int(result['rotation'])

    for x in cipher_original:
        ciphered_results += (letters[(letters.index(x) + rotation) % 26])

    print(cipher_original, rotation, ciphered_results)

    return render_template('result.html', cipher_original=cipher_original, rotation=rotation, ciphered_results=ciphered_results)
