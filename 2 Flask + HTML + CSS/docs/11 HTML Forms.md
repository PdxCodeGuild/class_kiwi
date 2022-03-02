
# HTML Forms

- [Overview](#overview)
- [Interactive Elements](#interactive-elements)
  - [Buttons: `button`](#buttons-button)
  - [Input: `input`](#input-input)
  - [Text Area: `textarea`](#text-area-textarea)
  - [Dropdown Lists: `select`](#dropdown-lists-select)
- [Attributes](#attributes)
  - [The Name Attribute](#the-name-attribute)
  - [The Value Attribute](#the-value-attribute)
  - [The Checked Attribute](#the-checked-attribute)
  - [The Placeholder Attribute](#the-placeholder-attribute)
  - [The Disabled Attribute](#the-disabled-attribute)
  - [The Required Attribute](#the-required-attribute)
  - [The Pattern Attribute](#the-pattern-attribute)

## Overview

A `form` is an HTML element that allows users to transmit data to a server. You can read more about forms [here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Your_first_HTML_form). There are 4 important parts to a form:

1. The `action` is the path or url to which the form's data will be submitted.
2. The `method` is the HTTP method to send the request in (POST, GET).
3. The `input` elements inside a form need `name` attributes, which will be used to retreive the data on the back-end.
4. The `<button type="submit">` or `<input type="submit">` will submit the form when clicked.

```html
<form action="myurl" method="post">
    <input type="text" name="myname"/>
    <button type="submit">submit</button>
</form>
```


## Interactive Elements

### Buttons: `button`

The `button` element creates a button, which can be used to trigger JavaScript events or submit forms. Keep in mind it's possible (and often easier) to make other elements (`a`, `div`, etc) *look* like buttons.

```html
<!-- buttons for javascript events -->
<button>click</button>
<button type="button">click</button>
<input type="button" value="click"/>

<!-- buttons for submitting a form -->
<button type="submit">submit</button>
<input type="submit" value="submit">
```

### Input: `input`

The `input` element can be used for a variety of different controls users to enter data. You can read more at [mdn](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) and [w3schools](https://www.w3schools.com/tags/tag_input.asp).

```html
<!-- a simple text input -->
<input type="text"/>
<!-- just like text input, but the text is hidden -->
<input type="password"/>

<!-- enter a number -->
<input type="number"/>
<!-- a slider -->
<input type="range">

<!-- enter a date -->
<input type="date">
<!-- enter a date and time -->
<input type="datetime-local">

<!-- enter a color -->
<input type="color"/>

<!-- radio buttons, functionally the same as select elements -->
<input type="radio"/>

<!-- checkbox -->
<input type="checkbox"/>
```

If radio buttons are given the same `name` attribute, only allow one among them can be selected at any time.

```html
<input type="radio" name="gender" value="male" checked> Male<br>
<input type="radio" name="gender" value="female"> Female<br>
<input type="radio" name="gender" value="other"> Other
```

### Text Area: `textarea`

The `textarea` element is a resizable multi-line text input.


```html
<textarea>hello world!</textarea>
```


### Dropdown Lists: `select`

A `select` tag defines a dropdown list. Each `option` defines an option of that dropdown list. Note that the `value` attribute differs from the inner text. The inner text servers human interests, the `value` serves the code's interests. Read more on [mdn](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) and [w3schools](https://www.w3schools.com/tags/tag_select.asp).

```html
<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
```


## Attributes

### The Name Attribute

The `name` attribute controls the name of the information submitted.

```html
<input type="text" name="fruit"/>
```

### The Value Attribute

The `value` attribute is used to set the starting value of an input element.

```html
<input type="text" value="llama">
```

### The Checked Attribute

The `checked` attribute controls whether a radio button or checkbox is checked.

```html
<input type="checkbox" checked>
```

### The Placeholder Attribute

You can also add a `placeholder` attribute to show some text in the 'background' of the input field. This text disappears when a value is entered.

```html
<input type="text" name="name" value="jane" placeholder="enter your name"/>
```

### The Disabled Attribute

To disabled an input field, you can add the `disabled` attribute without any parameters. This will prevent the user from entering any value into the input field. It doesn't matter what the value of the attribute is, as long as it's present, the input will be disabled.

```html
<input type="text" name="name" value="jane" disabled/>
```

### The Required Attribute

You can place the attribute `required` with no value to prevent the form from being submitted without that field being filled. Like `disabled`, the attribute doesn't need a value.

```html
<input type="text" name="name" required/>
```


### The Pattern Attribute

HTML5 brought the `pattern` attribute, which enables you to do validation entirely within HTML. You only have to enter a regular expression into the `pattern` attribute. If the user tries to submit the form and the given input doesn't match the pattern, a message will pop up containing the text in the `title` attribute.

```html
<input type="text" pattern="[a-z]{1,15}" title="username must be between 1 and 15 characters, all lowercase" required/>
```











