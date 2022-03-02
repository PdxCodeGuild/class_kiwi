# CSS Selectors

Selectors control which elements get applied a set of properties. You can find more info [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Simple_selectors), [here](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors), and [here](https://www.w3schools.com/cssref/css_selectors.asp). To get some practice with selectors, try [this](https://flukeout.github.io/).

- [Tag Selector: `tag`](#tag-selector-tag)
- [Class Selector: `.class`](#class-selector-class)
- [ID Selector: `#id`](#id-selector-id)
- [Attribute Selector: `element[attribute="value"]`](#attribute-selector-elementattributevalue)
- [Universal Selector: `*`](#universal-selector-)
- [Using Multiple Selectors: `,`](#using-multiple-selectors-)
- [Descendant Selector: `selector1 selector2`](#descendant-selector-selector1-selector2)
- [Child Selector: `selector1 > selector2`](#child-selector-selector1--selector2)


## Tag Selector: `tag`

If you just write the tag name as the selector, it'll select all tags of that type.

```html
<style>
    h1 {
        font-size:20px;
    }
</style>
<h1>hello world!</h1>
```

```html

p {
    font-size:12px;
}
```

## Class Selector: `.class`

Putting a `.` before a selector allows you to define a CSS class. This will apply to all elements with that class in their `class` attribute. A `class` attribute can contain multiple classes, separated by spaces.

```html
<style>
    .error {
        color: red;
        border: 1px solid red;
    }
    .warning {
        color: yellow;
        border: 1px solid yellow;
    }
</style>
<div class="error">This is an error message</div>
<div class="warning">This is a warning</div>
```

## ID Selector: `#id`

Putting a `#` in front of your selector lets you target the particular element with that `id`.

```html
<style>
    #paragraph1 {
        font-size: 12px;
    }
    #paragraph2 {
        font-size: 10px;
    }
</style>
<p id="paragraph1">blahblahblah</p>
<p id="paragraph2">blahblahblah</p>
```

## Attribute Selector: `element[attribute="value"]`

Using square brackets, you can select elements based on their attribute's value.

```html
<style>
    input[type="text"] {
      width: 100px;
    }
</style>
<input type="text">
```

## Universal Selector: `*`

Using a `*` will select everything, it's generally better to apply a style to the `body` tag and let descendants pick it up.


## Using Multiple Selectors: `,`

If you want to apply a set of properties using several different selectors, use a comma.

```html
<style>
    #btn1, #btn2 {
        color: white;
    }
</style>
<button id="btn1">this is selected</button>
<button id="btn2">this too!</button>
```


## Descendant Selector: `selector1 selector2`

To select all descendants, use a space ` `.

```html
<style>
    #outer .btn {
        color: red;
    }
</style>
<button class="btn">this won't be selected</button>
<div id="outer">
    <button class="btn">but this will</button>
    <div>
        <button class="btn">and so will this</button>
    </div>
</div>
```

## Child Selector: `selector1 > selector2`

To only select immediate children (not grand-children, great grand-children, etc), use `>`.

```html
<style>
    #outer > .btn {
        color: red;
    }
</style>
<button class="btn">this won't be selected</button>
<div id="outer">
    <button class="btn">this will</button>
    <div>
        <button class="btn">but this won't</button>
    </div>
</div>
```
