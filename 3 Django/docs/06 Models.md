

# Models

- [Overview](#overview)
- [Field Types](#field-types)
  - [Blankable Fields](#blankable-fields)
  - [Nullable Fields](#nullable-fields)
  - [Default Values](#default-values)
- [Database Relationships](#database-relationships)
  - [Many-to-One](#many-to-one)
  - [One-to-One](#one-to-one)
  - [Many-to-Many](#many-to-many)
  - [The On-Delete Parameter: `on_delete`](#the-on-delete-parameter-on_delete)
  - [The Related-Name Parameter: `related_name`](#the-related-name-parameter-related_name)
- [ORM Operations](#orm-operations)
  - [Example Models and Data](#example-models-and-data)
  - [Creating a Record](#creating-a-record)
  - [Getting a Record](#getting-a-record)
  - [Updating a Record](#updating-a-record)
  - [Get All Rows](#get-all-rows)
  - [Check if a Record Exists](#check-if-a-record-exists)
  - [Filter Rows](#filter-rows)
  - [Specify an Order](#specify-an-order)
  - [Specify the Number of Records to Return](#specify-the-number-of-records-to-return)
  - [Get the Number of Records](#get-the-number-of-records)
  - [Advanced ORM](#advanced-orm)


## Overview

Models are Python classes that parallel tables in the database. The ORM (object-relational mapping) manages this dual representation, translating statements in Python to queries on the database. You can read more about models [here](https://docs.djangoproject.com/en/3.2/topics/db/models/), and more about the ORM [here](https://docs.djangoproject.com/en/3.2/ref/models/querysets/). For ORM practice, check out the [Polls Tutorial - Part 2](https://docs.djangoproject.com/en/3.2/intro/tutorial02/).

Database tables are like spreadsheets: they have headers and rows. Tables can also be thought of as Python classes, where the headers are class attributes, and the rows are class instances. All models are automatically given an `id` field as a primary key, which is used to uniquely identifies a row.

| id | email_address | first_name | last_name |
| --- | --- | --- | --- |
| 1 | wendy@gmail.com | Wendy | Carson |
| 2 | alyssa@gmail.com | Alyssa	 | Lyons |
| 3 | brian@gmail.com | Brian | Barber |

```python
from django.db import models

# our contact model
class Contact(models.Model):
    email_address = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

# get the record with id=1 from the database, the first row
contact = Contact.objects.get(id=1)
# access the column value as a class attribute
print(contact.first_name) # Wendy

# create a new instance of our model, creating the third row
contact_new = Contact(first_name='Brian', last_name='Barber', email='brian@gmail.com')
contact_new.save() # save it to the database
```

## Field Types

The fields of a model create represent both the attribute of a class and the column of a table. You can read more about the field types [here](https://docs.djangoproject.com/en/3.2/ref/models/fields/). Below are some of the common fields used with a model.

- `BooleanField` represents a boolean (true/false) value
- `IntegerField` represents an integer
- `FloatField` represents a floating-point number
- `CharField` represents a string, requires `max_length` parameter indicating the number of characters
- `TextField` like `CharField` but has unlimited length
- `DateTimeField` represents a datetime (more [here](https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/))
- `OneToOneField` represents a [one-to-one relationship](https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/)
- `ForeignKey` represents a [many-to-one relationship](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/)
- `ManyToManyField` represents a [many-to-many relationship](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/)


### Blankable Fields

Fields that are marked `blank=True` allow the user to insert a blank value in the admin panel, which will result in a blank string for a `CharField` or `TextField`, or `null` for other field types.

```python
from django.db import models
class Contact(models.Model):
    ...
    favorite_color = models.CharField(blank=True) # the user can save a blank string in the admin panel
```


### Nullable Fields

Fields that are marked `null=True` are 'nullable', meaning they can have a null value. In Python, the attributes of the model will have a value of `None`. To save records with `null` value from the admin panel, you must also add `blank=True`. [more info] (https://www.geeksforgeeks.org/nulltrue-django-built-in-field-validation/)

```Python
from django.db import models

class TodoItem(models.Model)
    ...
    date_completed = models.DateTimeField(null=True, blank=True)
```

### Default Values

You can specify a default value for a field by adding `default=value`. That way, you can leave the value out when creating and saving an instance.

```python
from django.db import models

class BlogPost(models.Model):
    text = models.CharField()
    upvotes = models.IntegerField(default=0)
```

```python
blog_post = BlogPost(text="Lorem Ipsum") # no need to specify age, it will default to 0
blog_post.save()

blog_post2 = BlogPost(text="Delorum Est", upvotes=3) # we can specify if needed
blog_post2.save()
```


## Database Relationships

The three types of database relationships: one-to-one, many-to-one, and many-to-many. The `id` field of a table is called the **primary key** because it uniquely identifies a row. When another table contains a reference to that `id` field, it's called a **foreign key**.

### Many-to-One

A many-to-one relationship means that for every row in table A, there may be multiple rows in table B connected to it. An example might be between a [mother and her children](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/CPT-Databases-OnetoMany.svg/460px-CPT-Databases-OnetoMany.svg.png). A mother may have multiple children, but any child only has one mother. You can read more about many-to-one relationships [here](https://docs.djangoproject.com/en/2.1/topics/db/examples/many_to_one/).

In the following example, `city_id` on `Contact` is a **foreign key**, `id` on `Contact` and `id` on `City` are **Primary Keys**. This is an example of a **many-to-one relationship**.

**Contacts**
| id | first_name | last_name | email_address | city_id |
| --- | --- | --- | --- | --- |
| 1 | Wendy | Carson | wendy@gmail.com | 1 |
| 2  | Alyssa | Lyons | alyssa@gmail.com | 1 |
| 3  | Brian | Barber | brian@gmail.com | 2 |

**Cities**
| id | name |
| --- | --- |
| 1 | Portland |
| 2 | Eugene |


```python
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
```

Notice the `related_name` on the `ForeignKey` field. This controls how we refer to the list of all the `Contact`s for a given `City`. By default Django will take model name, make it lowercase, and add an `_set`, so if we did not specify `related_name` here it would be `contact_set`, but because we did, it will be `contacts`.

```python
contact = Contact.objects.get(first_name='Alyssa')
# only one city per contact
print(contact.city.name) # Portland

city = City.objects.get(name='Portland')
# multiple contacts for a given city
contacts = city.contacts.all()
print(contacts) # Wendy, Alyssa
```


### One-to-One

A one-to-one relationship means that for every row in table A, there will be a single corresponding row in table B. An example might be between [counties and capital cities](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/CPT-Databases-OnetoOne.svg/460px-CPT-Databases-OnetoOne.svg.png). A country only has one capital. A capital only pretains to one country. You can read more about one-to-one relationships [here](https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/). Normally a one-to-one relationship is unnecessary, because one could just take the fields from both models and put them onto one model. But you may have to associate new fields with an old model without changing the old model, or need to restrict access to certain data [more info](https://stackoverflow.com/questions/25206447/when-to-use-one-to-one-relationships-in-django-models).



**Capital**
| id | name |
| --- | --- |
| 1 | Washington DC |
| 2 | Mexico City |
| 3 | Ottawa |


**Country**
| id | name |
| --- | --- |
| 1 | The United States |
| 2 | Mexico |
| 3 | Canada |


```python
from django.db import models

class Capital(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.OneToOneField(Capital, on_delete=models.CASCADE, related_name='country')

    def __str__(self):
        return self.name
```

```python

capital = Capital.objects.get(name='Washington DC')
print(capital.country.name) # The United States

country = Country.objects.get(name='The United States')
print(country.capital.name) # Washington DC

# create a new capital
capital_city = Capital(name='Canberra')
capital_city.save()

# create a new city
country = Country(name='Australia', capital=capital_city)
country.save()
```

### Many-to-Many

An example of many-to-many relationships might be between [authors and books](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/CPT-Databases-ManytoMany.svg/460px-CPT-Databases-ManytoMany.svg.png). One book may have multiple authors. One author may have multiple books. A many-to-many relationship can be created in Django using a [ManyToManyField](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/). To maintain such a relationship in SQL, Django creates a [junction table](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Databases-ManyToManyWJunction.jpg/800px-Databases-ManyToManyWJunction.jpg) with two many-to-one relationships.



**Books**
| id | title |
| --- | --- |
| 1 | Good Omens |
| 2 | The Odyssey |
| 3 | The Illiad |


**Authors**

| id | name |
| --- | --- |
| 1 | Homer |
| 2 | Terry Pratchett |
| 3 | Neil Gaiman |


**Book-Authors**

| id | book_id | author_id |
| --- | --- | --- |
| 1 | 2 | 1 |
| 2 | 1 | 2 |
| 3 | 1 | 3 |



```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return self.title
```


```python
book = Book.objects.get(title='Good Omens')
authors = book.authors.all() # all the authors for a book
print(authors) # Terry Pratchett, Neil Gaiman

author = Author.objects.get(name='Homer')
books = author.objects.all() # all the books for an author
print(books) # The Odyssey, The Illiad
```


### The On-Delete Parameter: `on_delete`

The `on_delete` parameter lets you control what to do with other rows when a connected row is deleted. You can read more about `on_delete` [here](https://docs.djangoproject.com/en/3.2/ref/models/fields/#arguments). The important options are:

- `CASCADE` deleted this row when the other is deleted
- `PROTECT` throws an exception when the other is deleted, this forces the developer re-assign the relationship when they want to delete a row
- `SET_NULL` sets the field containing the relationship to null (the field must also be nullable)
- `SET_DEFAULT` sets the field containing the relationship to its default value (a default must be specified)

For example, consider the following models and data:

**Contacts**
| id | first_name | last_name | email_address | city_id |
| --- | --- | --- | --- | --- |
| 1 | Wendy | Carson | wendy@gmail.com | 1 |
| 2  | Alyssa | Lyons | alyssa@gmail.com | 1 |
| 3  | Brian | Barber | brian@gmail.com | 2 |

**Cities**
| id | name |
| --- | --- |
| 1 | Portland |
| 2 | Eugene |


```python
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
```

Note the `on_delete=models.CASCADE`, this means if we delete a `City`, all the `Contact`s associated with that `City` will automatically be deleted as well.

```python
city = City.objects.get(name='Portland')
city.delete() # also deletes the Contacts Wendy and Alyssa
```

###  The Related-Name Parameter: `related_name`

The `related_name` parameter controls what the name of the related class's attribute is. For example, consider the following models and data:

**Contact**
| id | first_name | last_name | email_address | city_id |
| --- | --- | --- | --- | --- |
| 1 | Wendy | Carson | wendy@gmail.com | 1 |
| 2  | Alyssa | Lyons | alyssa@gmail.com | 1 |
| 3  | Brian | Barber | brian@gmail.com | 2 |

**Cities**
| id | name |
| --- | --- |
| 1 | Portland |
| 2 | Eugene |


```python
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
```

Notice the `related_name` on the `ForeignKey` field. This controls how we refer to the list of all the `Contact`s for a given `City`. By default Django will take model name, make it lowercase, and add an `_set`, so if we did not specify `related_name` here it would be `contact_set`, but because we did, it will be `contacts`.

```python
contact = Contact.objects.get(first_name='Alyssa')
# only one city per contact
print(contact.city.name) # Portland

city = City.objects.get(name='Portland')
# multiple contacts for a given city
contacts = city.contacts.all()
print(contacts) # Wendy, Alyssa
```


## ORM Operations

The ORM 'object relational mapping' provides functions in Python that perform operations on the database. To read more about ORM operations, look [here](https://docs.djangoproject.com/en/3.2/topics/db/queries/). Note that `__init__`, `get`,  and `filter` take `**kwargs` (which turns named parameters into a dictionary), whereas `order_by` takes `*args` (which turns arguments into a list).

### Example Models and Data

**Contact**
| id | first_name | last_name | email_address | city_id |
| --- | --- | --- | --- | --- |
| 1 | Wendy | Carson | wendy@gmail.com | 1 |
| 2  | Alyssa | Lyons | alyssa@gmail.com | 1 |
| 3  | Brian | Barber | brian@gmail.com | 2 |
| 2  | Wendy | Clark | alyssa@gmail.com | 1 |

**Cities**
| id | name |
| --- | --- |
| 1 | Portland |
| 2 | Eugene |


```python
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
```


### Creating a Record

We create an instance of our model by invoking the class's initializer, which takes `kwargs`.

```python
contact = Contact(first_name='Alena', last_name='Deacon')
contact.save()
```

### Getting a Record

We can get a particular row using `get()` and passing the values of one or more attributes.

```python
# get a record using a single attribute
contact = Contact.objects.get(id=1)
print(contact) # Wendy Carson

# get a record using two attributes
contact = Contact.objects.get(first_name='Wendy', last_name='Carson')
print(contect) # Wendy Carson
```

An exception will occur if a record is not found. A safer way is to use `filter` (which gives us a list of matches) and `first` (which gives us the first result if there are any, and `None` if there isn't).

```python
contact = Contact.objects.filter(first_name='Alena').first()
print(contact) # None
```


### Updating a Record

We can update a record by assigning values to its attributes and saving.

```python
contact = Contact.objects.get(id=1)
contact.first_name = 'Cindy'
contact.save()
```


### Get All Rows

To get all the rows in a table use `all()`.

```python
contacts = Contact.objects.all()
print(contacts) # Wendy Carson, Alyssa Lyons, Brian Barber
```

### Check if a Record Exists

We can use `filter` (which gives us a list of matches) and `exists` (which return `True` if there are records, and `False` if there aren't).


```python
if Contact.objects.filter(first_name='Cindy').exists():
    ...
```

### Filter Rows

We can use `filter()` to get a list of records.

```python
contacts = Contact.objects.filter(first_name='Wendy')
print(contacts) # Wendy Carson, Wendy Clark
```

### Specify an Order

To specify an order, use `order_by`, which takes any number of strings containing the names of the fields to sort by. By default sort is ascending, use a negative symbol `-` to sort in the descending order.

```python
# sort by last name in ascending order
# then first name in descending order
contacts = Contact.objects.order_by('last_name', '-first_name')
```


### Specify the Number of Records to Return

To limit the number of items returned, use slicing.

```python
# only get the first 5 results
contacts = Contact.objects.all()[:5]
```

### Get the Number of Records


```python
contacts = Contact.objects.all().count()
```

### Advanced ORM

To filter variables by whether or not a field is null, use `<field_name>__isnull`
```python
completed_items = TodoItem.objects.filter(date_completed__isnull=False)
```