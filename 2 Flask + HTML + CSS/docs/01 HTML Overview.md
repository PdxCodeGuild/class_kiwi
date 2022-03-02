
# HTML Overview

[HTML](https://en.wikipedia.org/wiki/HTML) stands for 'hypertext markup language', hypertext meaning that it also contains multimedia such as images, sound, and video, markup language meaning it's for formatting. HTML is the skeleton of a page, forming its fundamental structure. HTML is displayed, not 'run' like Python. You can read more about HTML on the [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML) or [w3schools](https://www.w3schools.com/html/default.asp).

HTML5 is the latest standard of HTML, and includes support for canvas and video elements, semantic elements, and much more. All modern browsers support HTML5, but some older browsers may not. Certain businesses are limited to older browsers, so you may need to write code that's compatible with them. You can view browser compatibility [here](https://html5test.com/results/desktop.html).

The [DOM](https://en.wikipedia.org/wiki/Document_Object_Model) (Document Object Model) represents the hierarchical structure of [elements](https://en.wikipedia.org/wiki/HTML_element) that make up an HTML document.

- [HTML Syntax](#html-syntax)
- [HTML Attributes](#html-attributes)
  - [The Source Attribute: `src="file"`](#the-source-attribute-srcfile)
  - [The Href Attribute `href="file"`](#the-href-attribute-hreffile)
  - [The Title Attribute: `title="text"'](#the-title-attribute-titletext)
- [Void Elements](#void-elements)
- [Page Template](#page-template)
- [Meta Tags](#meta-tags)
- [Comments](#comments)
- [Block and Inline Elements](#block-and-inline-elements)
- [Preprocessors](#preprocessors)





## HTML Syntax

HTML elements (or 'tags') have three parts- the **element name**, **attributes** and **inner HTML** or **inner text**. Elements that contain other elements are called 'parents', elements contained in other elements are called 'children'. In general you should **use double quotes for attributes, and use lowercase for element names and attributes**.


```html
<div attribute="value">inner text</div>
<div attribute1="value1" attribute2="value2">
    <div>inner element</div>
</div>
```


## HTML Attributes

HTML elements can contain attributes which control their appearence and behavior.


### The Source Attribute: `src="file"`

The `src` attribute controls what external file is loaded, either by path or url.

```html
<img src="images/profile.jpg"/>
<img src="https://picsum.photos/200/300">
<script src="js/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.12"></script>
```

### The Href Attribute `href="file"`

The `href` attribute created a link to an external file.

```html
<a href="https://www.google.com/">link</a>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
```


### The Title Attribute: `title="text"'

The `title` attribute will show a 'tooltip' when the user hovers over the element. This can provide a helpful hint.

```html
<span title="hello world!">hover over me</span>
```

## Void Elements

Void or empty elements do not have closing tags, and including closing tags will produce an error. The slash at the end is optional, but it's more explicit to include it (otherwise it looks like an open tag with no closing tag). Common void elements include `br`, `hr`, `img`, `input`, `link`, and `meta`. You can view a full list [here](https://developer.mozilla.org/en-US/docs/Glossary/Empty_element). 

```html
<input type="text" value="ok"/>
<input type="text" value="also ok">
```


## Page Template

Below is general form of an HTML document. When the page loads it's read from the top down. External CSS and JS files can loaded anywhere in the page. JavaScript that references page elements (`getElementById`, `querySelector`) must appear after those page elements appear in the page, otherwise these functions will return `null`. CSS is ordinarily put in the head along with other metadata, JavaScript is ordinarily put at the bottom of the body so the document can load and be displayed to the user more quickly.

```html
<!DOCTYPE html>
<!-- root element -->
<html lang="en">
  <!-- the head contains metadata about the document  -->
  <head>
    <!-- meta tags store general metadata -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- page title, the text that appears on a browser -->
    <title>Demo Page</title>
    <!-- import external css -->
    <link rel="stylesheet" type="text/css" href="css/index.css"/>
  </head>
  <!-- the body contains the actual document that will be shown to the user -->
  <body>
    <!-- page element -->
    <p>Hello world!</p>
    <!-- import external javascript  -->
    <script type="text/javascript" src="js/index.js"></script>
  </body>
</html>
```


- The `DOCTYPE` tag tells the browser that the document contains HTML. If omitted, some browsers will revert [quirks mode](https://en.wikipedia.org/wiki/Quirks_mode) for rendering.
- The `html` tag contains the entire document
- The `head` tag contains metadata, nothing inside of it is rendered in the page.
    - The `title` tag contains the text that's displayed in the browser tab, or the top of the browser window. It should contain the site name and a page name.
- The `body` tag contains the document's content, what will be shown to the user
- the `p` tag represents a paragraph


## Meta Tags

```html
<meta name="author" content="Your Name">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Comments

Comments in HTML are represented by a special tag, beginning with an explanation point and two hyphens, and ending with two hyphens.

```html
<!-- this is a comment -->
```

## Block and Inline Elements

[Block](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) elements will take up the full available width and force other elements to move to a new line. Examples of block elements are `p`, `h1`, `div`, `ol`/`ul`, and `form`.

[Inline](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements) elements only take the amount of space they need, and allow other elements to exist on the same line. Examples of inline elements are `span`, `img`, and `a`.





## Preprocessors

There are several HTML preprocessors: [Haml](http://haml.info/), [Jade](http://jade-lang.com/), [Slim](http://slim-lang.com/index.html), and [Markdown](https://en.wikipedia.org/wiki/Markdown).

