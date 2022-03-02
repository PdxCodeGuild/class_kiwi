
# Flask Forms

When a Flask view receives a form submission, it's transformed into a dictionary and is accessable as `request.form`. By default, routes only respond to GET requests, we can allow them to respond to requests using other methods by passing them to the `route`.

**index.html**
```html
<form action="" method="post">
  <input type="text" name="input_text" placeholder="enter some text"/>
  <button type="submit">submit</button>
</form>
```

**app.py**
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
    return render_template('index.html')
```


You can also use two separate views, one for rendering a template, and another for receiving a form submission and redirecting back to the first view.


**index.html**
```html
<form action="/receive_form/" method="post">
    <input type="text" name="person_name" value="Jane"/>
    <input type="text" name="person_age" value="34"/>
    <button type="submit">submit</button>
</form>
```

**app.py**
```python
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_form/', methods=['POST'])
def temperature():
    print(request.form) # {'person_name': 'Jane', 'person_age': 34}
    person_name = request.form['person_name'] # Jane
    person_age = request.form['person_age'] # 34
    return redirect('/')
```
