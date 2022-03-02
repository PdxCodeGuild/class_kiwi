
# CSS Overview

CSS stands for [Cascading Style Sheets](https://en.wikipedia.org/wiki/Cascading_Style_Sheets), "cascading" meaning that style rules are evaluated by priority. That is, if a style rule is applied to a particular element, it'll override the rules applied to its parent. Whereas HTML is the raw skeleton of a page, CSS adds fonts, colors, margins, positioning, animations, and more.


- [CSS Syntax](#css-syntax)
- [Priority](#priority)
- [Including CSS](#including-css)
  - [Inline CSS](#inline-css)
  - [Style Tag](#style-tag)
  - [External CSS](#external-css)
- [Removing the Browser's Built-In CSS](#removing-the-browsers-built-in-css)
- [CSS Preprocessors](#css-preprocessors)
- [Resources](#resources)
- [Libraries](#libraries)


## CSS Syntax

CSS has two major parts: properties and selectors. Properties set the color, shape, positioning, etc of elements. Selectors determine what HTML elements receive the given properties.

```css
selector {
    property: value;
}
```

You can add comments in CSS with `/* ... */`

```css
/* this is for a very special div,
 * one that requires lots of explanation
 */
div {
    color: #0FA0CE; /* a beautiful color */
}
```


## Priority

CSS Rules will be applied with the following priority (highest first). You can place a special keyword on rules which will automatically give them the highest priority.

```css
div {
    /* overwrite all other rules */
    color: red !important;
}
```

| Priority | Definition |
|--- |--- |
| 1 | rules with `!important` |
| 2 | inline style |
| 3 | media queries |
| 4 | user-defined (through developer panel) |
| 5 | internal and external CSS, by last defined rule |
| 6 | parent element's value |
| 7 | browser default |

## Including CSS

There are three ways to add CSS to a page.

### Inline CSS

The simplest and quickest way to write CSS is inside a HTML tag's `style` attribute. CSS properties are separated via semi-colons.

```html
<div style="color:blue;background-color:DarkOliveGreen">This is some ugly text</div>
```

Inline styles are fine when experimenting, but consider the following case.

```html
<ol>
    <li style="color:red">Apple</li>
    <li style="color:red">Banananana</li>
    <li style="color:red">Pear</li>
</ol>
```

This can become tedious to work with, because we have to edit the same value in multiple places. Therefore, it's generally better to use a style tag.

### Style Tag

CSS can be placed within its own tag, usually inside the document's `head`. This way your CSS is not tied to any particular element and is all in one place. This makes your code more organized and manageable. The `type` attribute isn't necessary for HTML5, but it is for HTML4 and below.

```html
<html>
    <head>
        <style type="text/css">
            li {
                color:red;
            }
        </style>
    </head>
    <body>
        <ol>
            <li>Apple</li>
            <li>Banananana</li>
            <li>Pear</li>
        </ol>
    </body>
</html>
```

### External CSS

You can also keep css in external files. This is useful if you want to use the same CSS across multiple pages. The `link` tag should also go inside the `head`. The `type="text/css"` isn't necessary for HTML5, but it is for HTML4 and below. Be aware that it's **common for your browser to cache external CSS, and you won't see changes you've made until you do a "hard refresh".** You can find out how to do this in various browsers [here](https://en.wikipedia.org/wiki/Wikipedia:Bypass_your_cache).

```html
<link rel="stylesheet" type="text/css" href="mystyle.css"/>
```

You can also include CSS from a remote server by putting a URL in `href`. Your browser will download the CSS when the page is rendered. This is commonly served by a CDN "content delivery network".

```html
<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
```



## Removing the Browser's Built-In CSS

You can remove the browser's built-in css by including [normalize.css](http://necolas.github.io/normalize.css/) or [reset.css](https://meyerweb.com/eric/tools/css/reset/). You can read about the differences [here](https://stackoverflow.com/questions/6887336/what-is-the-difference-between-normalize-css-and-reset-css).


## CSS Preprocessors

The two most popular CSS preprocessors are [Sass/SCSS](http://sass-lang.com/) and [Less](http://lesscss.org/). For info on using CSS preprocessors in PyCharm, look [here](https://www.jetbrains.com/help/pycharm/compiling-sass-less-and-scss-to-css.html).

[inspiration for design elements](https://get.foundation/building-blocks/index.html)

## Resources

- Learning
  - [CSS Diner](https://flukeout.github.io/): practice css selectors
  - [Grid Garden](https://cssgridgarden.com/): practice css grid
  - [Flexbox Froggy](http://flexboxfroggy.com/) and [Flexbox Defense](http://www.flexboxdefense.com/): practice css flexbox
- Reference
  - [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
  - [A Complete Guide to Grid](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- Images
  - [Unsplash](https://unsplash.com/)
  - [Pixabay](https://pixabay.com/)
- Icons
  - [Simple Icons](https://simpleicons.org/)
  - [Noun Project](https://thenounproject.com/)
- Color
  - [Adobe Color](https://color.adobe.com/create/color-wheel)
  - [List of Color Names](https://htmlcolorcodes.com/color-names/)
  - [Coolers](https://coolors.co/)
  - [Canva Colors](https://www.canva.com/colors/color-palette-generator/)
- Lorem Ipsum Generators
  - [Meet the Ipsums](https://meettheipsums.com/)
  - [Ultimate List of Lorem Ipsum Generators](https://loremipsum.io/ultimate-list-of-lorem-ipsum-generators/)
  - [List on Mashable](https://mashable.com/2013/07/11/lorem-ipsum/)
- Photo Editing Programs
  - [Glimpse](https://glimpse-editor.org/)
  - [Paint.NET](https://www.getpaint.net/) (Windows only)
- Mockups


## Libraries

CSS frameworks can be used to make your site look pretty quickly and easily. Each framework has its own style and number of features. You can view a long list [here](https://github.com/troxler/awesome-css-frameworks) and another [here](https://www.keycdn.com/blog/frontend-frameworks).

- [Bootstrap](http://getbootstrap.com/), [w3schools tutorial](https://www.w3schools.com/bootstrap4/default.asp)
- [Materialize](http://materializecss.com/)
- [Pure.css](https://purecss.io/)
- [Foundation](http://foundation.zurb.com/sites/docs/)
- [Skeleton](http://getskeleton.com/)
- [Material Design](https://material.io/guidelines/#)
- [Kube](https://imperavi.com/kube/)
- [Milligram](http://milligram.io/)
- [Bulma](http://bulma.io/)
- [Vuetify](https://vuetifyjs.com/) (for use with Vue.js)
- [Material UI](http://www.material-ui.com/#/) (for use with React)
- [fontawesome.com](https://fontawesome.com/) (icons)


