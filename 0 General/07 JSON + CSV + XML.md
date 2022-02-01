
# JSON, CSV, & XML

JSON, CSV, and XML are three popular ways of storing and sending data.

- [JSON](#json)
- [CSV](#csv)
- [XML](#xml)

## JSON


[JSON](http://www.json.org/) stands for "JavaScript Object Notation", and looks similar to JavaScript objects and Python Dictionaries. The major difference is that the values can only be objects, arrays, numbers, strings, booleans, or null. You can read more about the differences between JSON and JavaScript objects [here](https://stackoverflow.com/questions/8294088/javascript-object-vs-json). JSON can be stored in plain text files with the `.json` extension.

```json
{"employees":[
    { "firstName":"John", "lastName":"Doe" },
    { "firstName":"Anna", "lastName":"Smith" },
    { "firstName":"Peter", "lastName":"Jones" }
]}
```

Python has the built-in library `json` for converting dictionaries into json and back again.

```python
import json
person = {'name': 'jane', 'age': 34} # python dictionary
json_person = json.dumps(person) # convert a dictionary to a string containing json
person = json.loads(json_person) # convert a string containing json to a dictionary
```

```javascript
let person = {name: 'jane', age: 34} // javascript object
let json_person = JSON.stringify(person) // convert a javascript object into a string containing json
person = JSON.parse(json_person) // convert a string containing json into a javascript object
```

## CSV

CSV stands for "Comma-Separated Values" and is used to store tabular data. CSV data can be stored in plain text files with the `.csv` extension.

```csv
name,age,fav_color
jane,34,blue
joe,32,red
```

Python has a built-in library [csv](https://docs.python.org/3/library/csv.html) for parsing CSV files. There are a number of third-party libraries for parsing CSV data in JavaScript [node-csv-parse](https://csv.js.org/parse/), [Papa Parse](https://www.papaparse.com/), [csv.js](https://github.com/okfn/csv.js/).



## XML

[XML](https://developer.mozilla.org/en-US/docs/XML_Introduction) resembles HTML, it has tags, and attributes, and inner text.

```xml
<employees>
    <employee>
        <firstName>John</firstName>
        <lastName>Doe</lastName>
    </employee>
    <employee>
        <firstName>Anna</firstName>
        <lastName>Smith</lastName>
    </employee>
    <employee>
        <firstName>Peter</firstName>
        <lastName>Jones</lastName>
    </employee>
</employees>
```

Python has the [ElementTree](https://docs.python.org/3.8/library/xml.etree.elementtree.html) module to handle XML files. JavaScript has an [XMLSerializer and DOMParser](https://developer.mozilla.org/en-US/docs/Web/Guide/Parsing_and_serializing_XML).
