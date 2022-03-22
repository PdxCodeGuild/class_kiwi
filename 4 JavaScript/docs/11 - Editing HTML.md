
# Editing HTML

- [Overview](#overview)
- [Accessing Elements](#accessing-elements)
- [Setting innerText and innerHTML](#setting-innertext-and-innerhtml)
- [Editing Style](#editing-style)
- [Editing Classes](#editing-classes)
- [Setting Data](#setting-data)
- [Editing Attributes](#editing-attributes)
- [Input Fields](#input-fields)
  - [Text Input](#text-input)
  - [Radio Buttons and Checkboxes](#radio-buttons-and-checkboxes)
  - [Dropdown Lists](#dropdown-lists)
- [Creating and Adding Elements](#creating-and-adding-elements)


## Overview

JavaScript provides many functions to manipulate the DOM. You can find more info on [MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents) and [w3schools](https://www.w3schools.com/js/js_htmldom_document.asp).

## Accessing Elements

You can access the elements of the DOM from JavaScript using several functions. You can find more info on these functions [here](https://javascript.info/searching-elements-dom).


| function | description |
| ---      | ---         |
| `document.querySelector(selector)` | get an element that matches the given CSS selector |
| `document.querySelectorAll(selector)` | get all elements that match the given CSS selector |
| `document.getElementById(id)` | get an element with the given id |
| `document.getElementsByTagName(tag)` | get all elements of the given tag |
| `document.getElementsByName(name)` | get all elements with the given name |

The following code demonstrates how each of these are used:

```html
<div id="mydiv" name="adiv" class="myclass"></div>
<div id="thisdiv" class="myclass"></div>
<div id="thatdiv" name="adiv"></div>

<script>
    let a = document.getElementById('mydiv');
    let bs = document.getElementsByTagName('div');
    console.log(bs.length); // 3
    let cs = document.getElementsByName('adiv');
    console.log(cs.length); // 2
    let d = document.querySelector('#mydiv');
    let es = document.querySelectorAll('.myclass');
    console.log(es.length); // 2
</script>
```


## Setting innerText and innerHTML

You can set the text between a open and close tag (`<div>this</div>`) using `innerText` and `innerHTML`. As you might guess, `innerText` is for text, `innerHTML` is for a string containing HTML.

```html
<div id="div1"></div>
<div id="div2"></div>
<script>
    let div1 = document.querySelector('#div1');
    div1.innerText = "Hello World!";

    let div2 = document.querySelector('#div2');
    div2.innerHTML = "<p><b>Hello World!</b></p>";
</script>
```
This renders the following:

```html
<div id="div1">Hello World!</div>
<div id="div2"><p><b>Hello World!</b></p></div>
```

## Editing Style

You can assign attributes to elements just as you'd assign attributes to objects.

```html
<div id="demo_div"></div>
<script>
    let demo_div = document.querySelector('#demo_div');
    demo_div.innerHTML = "Hello World!";
    demo_div.style.fontSize = '24px';
    demo_div.name = "demo_div";
</script>
```

This renders the following:

```html
<div id="demo_div" style="font-size:24px" name="demo_div">Hello World!</div>
```

## Editing Classes

HTML elements have a special [classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) property can be used to add or remove CSS classes.



```javascript
// <div id="mydiv"></div>
mydiv.classList.add("class1");
// <div id="mydiv" class="class1"></div>
mydiv.classList.add("class2");
// <div id="mydiv" class="class1 class2"></div>
mydiv.classList.remove("class1");
// <div id="mydiv" class="class2"></div>
mydiv.classList.replace("class2", "class2");
// <div id="mydiv" class="class1"></div>
mydiv.classList.toggle("class1");
// <div id="mydiv" class=""></div>
mydiv.classList.toggle("class1");
// <div id="mydiv" class="class1"></div>
```

## Setting Data

HTML elements have a [dataset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOrForeignElement/dataset) property for storing and retrieving pieces of data.




## Editing Attributes

There are [multiple ways](https://stackoverflow.com/questions/3919291/when-to-use-setattribute-vs-attribute-in-javascript) to set attributes on HTML elements.

```html
<button id="btn">click</button>
<script>
  let btn = document.querySelector('#btn')
  btn.disabled = 'disabled'
  // <btn id="btn" disabled="disabled">click</button>
</script>
```

There are also methods for modifying attributes:

- `element.setAttribute(attribute_name, value)`
- `element.getAttribute(attribute_name)`
- `element.hasAttribute(attribute_name)`
- `element.removeAttribute(attribute_name)`

## Input Fields

Input elements allow the user to input their information [more info](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). The various input types may look different on different browsers.


### Text Input

```html
<input id="user_input" type="text"/>
<script>
    let text_field = document.querySelector('#user_input')
    let user_input = text_field.value
</script>
```


### Radio Buttons and Checkboxes

Checkboxes and radio buttons have a special `checked` attribute.


```html
<input id="cb_agree" type="checkbox"> I agree to the above conditions
<script type="text/javascript">
  let cb_agree = document.querySelector('#cb_agree')
  let checked = cb_agree.checked
  alert(checked)
</script>
```

If radio buttons are given the same `name` attribute, only allow one among them can be selected at any time. We can get the value of the selected radio button by selecting the radio button with the `checked` attribute.

```html
<input type="radio" name="fruit" value="Apples" checked> Apples<br>
<input type="radio" name="fruit" value="Bananas"> Bananas<br>
<input type="radio" name="fruit" value="Pears"> Pears
<script type="text/javascript">
  let fruit = document.querySelector('input[name="fruit"]:checked').value
</script>
```

### Dropdown Lists

A `select` tag defines a dropdown list. Each `option` defines an option of that dropdown list. Note that the `value` attribute differs from the inner text. The inner text servers human interests, the `value` serves the code's interests.

```html
<select id="ddl">
    <option value="volvo" selected>Volvo</option>
    <option value="saab">Saab</option>
    <option value="mercedes">Mercedes</option>
    <option value="audi">Audi</option>
</select>
<script>
    let ddl = document.querySelector('#ddl')
    console.log(ddl.value) // volvo
    console.log(ddl.options[ddl.selectedIndex].value) // alternatively
</script>
```

## Creating and Adding Elements

We can also create elements and add them to other elements.

| function | description |
| ----     | ----        |
| `document.createElement(tag_name)` | create an element with tag `tag_name` |
| `document.createTextNode(text)` | create a text node containing the given text (just set innerText instead) |
| `element.appendChild(child)` | append a child element to a parent element |
| `element.removeChild(child)` | remove a child element from a parent element |
| `element.hasChild(child)` | indicates whether the parent has a particular child |
| `element.replaceChild(child)` | replaces a child |


**Example - Building a Button**
```html
<div id="container_div"></div>
<script>
    let container_div = document.querySelector('#container_div')

    let btn = document.createElement("button")
    btn.style.backgroundColor = "lightblue"
    btn.style.border = "1px solid white"
    btn.innerText = 'click'

    container_div.appendChild(btn)
</script>
```
```html
<div id="container_div">
  <button style="background-color:lightblue;border:1px solid white">click</button>
</div>
```


**Example - Building a Select**
```html
<select id="select_fruits"></select>
<script>
    let select_fruits = document.querySelector('#select_fruits')
    let fruits = ['apples', 'bananas', 'pears']
    for (let i=0; i<fruits.length; ++i) {
        let option = document.createElement('option')
        option.innerText = fruits[i]
        option.value = fruits[i]
        select_fruits.appendChild(option)
    }
</script>
```
```html
<select id="select_fruits">
    <option value="apples">apples</option>
    <option value="bananas">bananas</option>
    <option value="pears">pears</option>
</select>
```