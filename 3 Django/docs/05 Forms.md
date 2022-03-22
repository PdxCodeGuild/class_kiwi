

# Forms

- [Overview](#overview)
- [Django Forms](#django-forms)
  - [The ModelForm Class](#the-modelform-class)
  - [Using Forms with CSS Frameworks](#using-forms-with-css-frameworks)



## Overview

A `form` is an HTML element that can transmit data from the front-end (client) to the back-end (server). Read more about forms [here](../../2%20Flask%20+%20HTML%20+%20CSS/docs/11%20HTML%20Forms.md). There are 5 important parts to a form:

1. The `action` is the path or url to which the form's data will be submitted.
2. The `method` is the HTTP method to send the request in (POST, GET).
3. The `input` elements inside a form need name attributes, which will be used to retreive the data on the back-end.
4. The `<button type="submit">` or `<input type="submit">` will submit the form when clicked.
5. The `{% csrf_token %}` will insert a token that protects against [Cross-site request forgeries](https://en.wikipedia.org/wiki/Cross-site_request_forgery).

```html
<form action="{% url 'contacts:save_contact' %}" method="post">
    {% csrf_token %}
    <input type="text" name="first_name"/>
    <input type="text" name="last_name"/>
    <button type="submit">save</button>
</form>
```

Django will take the key-value pairs from the form data in the request and put them into a dictionary-like object `request.POST`. You can then access those values from the view using the value of the `name` attribute as a key.


```python
def save_contact(request): # a view for receiving a form submission
    print(request.POST) # verify we received the form data
    first_name = request.POST['first_name'] # get the value the user entered into the 'first name' field
    last_name = request.POST['last_name'] # get the value the user entered into the 'last name' field
    contact = Contact(first_name=first_name, last_name=last_name) # create an instance of our model
    contact.save() # save a new row to the database
    ...
```

## Django Forms

Django has a special Form class to make the creation of forms easier. These also do input validation on the front-end and the back-end for you. You can read in the official docs: [Working with Forms](https://docs.djangoproject.com/en/4.0/topics/forms/), [Forms API](https://docs.djangoproject.com/en/4.0/ref/forms/api/#django.forms.Form). You can put your forms in a `forms.py` inside your app.


**forms.py**
```python
from django import forms
class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Contact Name', max_length=100)
    contact_age = forms.IntegerField(label='Contact Age')
```

**views.py**
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
def index(request):
    if request.method == 'POST': # receiving a form submission
        # create an instance of our form from the form data
        form = ContactForm(request.POST)
        if form.is_valid():
            # get the data out of the form
            contact_name = form.cleaned_data['contact_name']
            contact_age = form.cleaned_data['contact_age']
            # create an instance of our model from the data
            contact = Contact(name=contact_name, age=contact_age)
            # save a new record to the database
            contact.save()
            # create a new blank form for the template
            form = ContactForm()
        # if the form is invalid, we just send it back to the template
    else: # receiving a GET request
        form = ContactForm() # create a new blank form
    return render(request, 'contacts/index.html', {'form': form}) # pass the form to the template
```

**index.html**
```html
<form action="{% url 'contacts:index' %}" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>
```


### The ModelForm Class

ModelForms allow us to generate a form directly from a model. You can read more about ModelForms in the [official docs](https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/).

**models.py**
```python
from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

**forms.py**
```python
from django.forms import ModelForm
from .models import Contact
class TodoForm(ModelForm):
    class Meta:
        # the model to associate with the form
        model = Contact
        # a list of all the models' fields you want in the form
        # fields = ['text']
        # or just use all of them
        fields = '__all__'
```

**views.py**
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
def index(request):
    if request.method == 'POST': # receiving a form submission
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # save the todo item associated with the form
            form = ContactForm() # create a new blank form
        # if the form is invalid, we just send it back to the template
    else: # receiving a GET request
        form = ContactForm() # create a new blank form
    return render(request, 'contacts/index.html', {'form': form}) # pass the form to the template
```

**index.html**
```html
<form action="{% url 'contacts:index' %}" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>
```

### Using Forms with CSS Frameworks

CSS Frameworks like Boostrap and Materialize have specific ways their forms are structures, and don't work with the default forms very well. [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) allow you to better control how forms are rendered.

- [tutorial on using bootstrap w/ django forms](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)
- [library for using materialize w/ django forms](https://pypi.org/project/crispy-forms-materialize/)
