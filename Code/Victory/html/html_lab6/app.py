from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/code_cyph', methods=['POST'])
def code_cyph():
    result= request.form
    user_mess=result['message']
    rot_num = int(result['code'])

    new_message = ""

    for q in range(len(user_mess)):
        value_index = ord(user_mess[q])

        if value_index + rot_num > 122:
            new_rot = ((value_index+ rot_num)-122) % 26
            new_message += chr(new_rot + 96)
        else:
            new_message += chr(value_index + rot_num)
    print(user_mess,rot_num,new_message)
    

    return render_template('result.html', user_mess=user_mess, rot_num=rot_num, new_message=new_message )


if __name__ == "__main__":
    app.run(debug=True)


