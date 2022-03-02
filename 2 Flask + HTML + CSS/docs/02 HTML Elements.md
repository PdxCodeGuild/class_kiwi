
# HTML Elements

HTML elements make up the structure of a page. Many of these come with default styling from the browser. However all can be altered using CSS, thus their meaning is largely what you give to them. For a complete list of tags, look [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) and [here](https://www.w3schools.com/tags/).


- [Overview](#overview)
  - [Common Elements](#common-elements)
  - [Interactive Elements](#interactive-elements)
  - [Semantic Elements](#semantic-elements)
  - [Common Attributes](#common-attributes)
- [Common Elements](#common-elements-1)
  - [Header Tags: `h1`, `h2`, etc](#header-tags-h1-h2-etc)
  - [Paragraph Tags: `p`](#paragraph-tags-p)
  - [Quotes and Block-Quotes: `q`, `blockquote`](#quotes-and-block-quotes-q-blockquote)
  - [Pre-formatted Text: `pre`](#pre-formatted-text-pre)
  - [Lines and Breaks: `hr`, `br`](#lines-and-breaks-hr-br)
  - [Anchor Tags: `a`](#anchor-tags-a)
  - [Image Tags: `img`](#image-tags-img)
  - [Division Tags: `div`](#division-tags-div)
  - [Span Tags: `span`](#span-tags-span)
  - [Tables: `table`, `tr`, `th`, `td`](#tables-table-tr-th-td)
  - [Ordered and Unordered Lists: `ol`, `ul`](#ordered-and-unordered-lists-ol-ul)
- [Text Formatting Elements](#text-formatting-elements)



## Overview

### Common Elements

| element | description |
|---  |---    |
| [h1, h2, etc](#header-tags) | headers |
| [p](#paragraph-tags) | paragraph |
| [q](#quotes-and-block-quotes) | quote |
| [blockquote](#quotes-and-block-quotes) | block quote |
| [pre](#pre-formatted-text) | pre-formatted text |
| [hr](#lines-and-breaks) | horizontal line |
| [br](#lines-and-breaks) | line break |
| [a](#anchor-tags) | link, uses attribute `href` |
| [img](#image-tags) | image, uses attributes `src`, ` |
| [div](#division-tags) | division, block element, used to organize elements |
| [span](#span-tags) | span, inline element, used to organize elements |
| [table, tr, td, th](#tables) | table, row, column, header |
| [ol, ul, li](#ordered-and-unordered-lists) | ordered list, unordered list, list item |


### Interactive Elements

| element | description |
|---  |---    |
| [buttons](#button) | button |
| [input](#input) | various forms of input, uses attribute `type` |
| [select, option](#dropdown-lists) | drop-down list |


### Semantic Elements

You can read more about semantic elements [here](https://www.w3schools.com/html/html5_semantic_elements.asp).

| element | description |
|---  |---    |
| article | an article |
| aside | for content set aside (a sidebar) |
| details | additional details the user can show or hide |
| figure | a figure |
| figcaption | the caption for a figure |
| footer | the footer of a page |
| header | the header of a page |
| main | the main content of a page
| nav | a set of navigation links |
| section | a section of a page |
| summary | a summary |


### Common Attributes

| attribute | description |
|--- |--- |
| id | a unique identifier |
| style | inline css |
| class | css class |
| name | used when submitting data from a form |
| title | tool-tip, text that's displayed on mouse hover |
| src | source - used on `img` and `script` tags |
| href | reference - used on `a` and `link` tags |
| alt | used in `img` tags to display text when loading the image fails |
| width, height | used on `img` and `canvas` tags |


## Common Elements

### Header Tags: `h1`, `h2`, etc

The header (`h1`, `h2`, etc) let us define titles.

```html
<h1>This is ordinarily used for the title</h1>
<h2>This is a chapter title</h2>
<h3>This is a sub-chapter title</h3>
<h4>and so on...</h4>
<h5>and so on...</h5>
```

### Paragraph Tags: `p`

The paragraph `p` tag lets us define paragraphs

```html
<p>Lorem ipsum dolor sit amet, consectetur...</p>
<p>Suspendisse elementum enim sed consectetur...</p>
<p>Donec at ligula hendrerit....</p>
```

### Quotes and Block-Quotes: `q`, `blockquote`

```html
<q>this is a quote</q>

<blockquote>This is a blockquote. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam consectetur nisi nec orci maximus, at facilisis lorem dignissim. Fusce vitae orci pharetra, facilisis dui ut, ullamcorper ex.</blockquote>
```

### Pre-formatted Text: `pre`

The `<pre>` tag allows pre-formatted text, and preserves spaces and line breaks.

```html
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
```

### Lines and Breaks: `hr`, `br`

The two tags `<hr/>` and `<br/>` are used without closing tags, and represent a broad horizontal line and line break respectively.

### Anchor Tags: `a`

The anchor tag `a` lets us create links.

```html
<a href="http://www.google.com">click this</a>
```

You can also create "internal links", which will take you do another part of the page. This is commonly done to make a table of contents. Note how the `href` begins with a `#` and takes us to the element with the matching `id`.

```html
<a href="#myheading">go to My Heading</a>
<h2 id="myheading">My Heading</h2>
```


### Image Tags: `img`

An `img` tag lets us display an image. The `src` attribute can be a relative path or a url. The `alt` is the text that will be displayed if the image fails to load.

```html
<img src="http://www.ackermanplumbing.com/ackermanplumbingserviceslogo.png" alt="Ackerman Plumbing" width="50" height="50"/>
```



### Division Tags: `div`

The `div` tag represents a generic block-level container.

```html
<div>This is a generic division</div>
```


### Span Tags: `span`

The `span` tag represents a generic inline-level container.

```html
<span>This is a generic span</span>
```


### Tables: `table`, `tr`, `th`, `td`

Table are defined first by row, then by column.

```html
<table>
    <tr>
        <td>A</td>
        <td>B</td>
    </tr>
    <tr>
        <td>C</td>
        <td>D</td>
    </tr>
    <tr>
        <td>E</td>
        <td>F</td>
    </tr>
</table>
```

Tables can also contain a top row of `th` 'table head' tags:

```html
<table>
 <tr>
   <th>Month</th>
   <th>Savings</th>
 </tr>
 <tr>
   <td>January</td>
   <td>$100</td>
 </tr>
</table>
```



### Ordered and Unordered Lists: `ol`, `ul`

Unordered lists are shown with bullet points, ordered lists are shown with numbers.

```html
<ul>
    <li>Apple</li>
    <li>Banananana</li>
    <li>Pear</li>
</ul>

<ol>
    <li>Apple</li>
    <li>Banananana</li>
    <li>Pear</li>
</ol>
```


## Text Formatting Elements

You can read more about text formatting elements [here](https://www.w3schools.com/html/html_formatting.asp). The elements `b`/`strong` and `i`/`em` will produce the same visual results, but there is a [semantic difference](https://stackoverflow.com/questions/271743/whats-the-difference-between-b-and-strong-i-and-em) between them.

| element | description |
|---  |---    |
| b | bold text |
| strong | important text, usually bold |
| i | italic text |
| em | emphasized text, usually italic |
| mark | marked or highlighted text |
| small | small text |
| del | deleted text (line-through) |
| ins | inserted text (underlined) |
| sub | subscript text |
| sup | superscript text |
| time | identify a time "11:23" within text |

```html
<p>Text formatting elements are meant to be embedded within text and determine how the text is rendered. They allow you to create <b>bold text</b> and <strong>strong text</strong>, <i>italic</i> and <em>emphasized</em> text, <mark>marked</mark>, <small>small</small>, <del>deleted</del>, <ins>inserted</ins>, <sub>subscript</sub>, <sup>superscript</sup>, and time <time>11:23</time>.</p>
```





