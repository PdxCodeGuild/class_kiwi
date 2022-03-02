

# Flask Todo List

Let's build a todo list with Flask and a simple database that uses JSON to store the data.

## Part 1

Create a folder for your lab, and inside of that create a `db.json` with the following contents:

**db.json**
```json
{
  "todos":[
    {
      "text": "walk the dog",
      "priority": "high"
    },{
      "text":"butter the cat",
      "priority":"medium"
    },{
      "text":"wash dishes",
      "priority":"low"
    }
  ]
}
```

Next, write a Flask app that uses the [JsonDB](jsondb.py) class to load the database and render a template containing the information. The resulting HTML should look something like this, but feel free to use a `table` or `div`s instead.

```html
<ul>
  <li>walk the dog (high)</li>
  <li>butter the cat (medium)</li>
  <li>wash dishes (low)</li>
</ul>
```

## Part 2

Using a `form`, allow the user to save a new todo item to the database. This should include a `input` for text, a `select` for the priority, and a `button` for submitting the form.

