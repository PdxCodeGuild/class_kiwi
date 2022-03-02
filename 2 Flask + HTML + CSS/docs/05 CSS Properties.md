
# CSS Properties

CSS properties allow you to control visual aspects of an HTML element. For more info, look [here](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) and [here](https://www.w3schools.com/cssref/).

- [CSS Lengths](#css-lengths)
- [CSS Colors](#css-colors)



| Property           | Values                                                    | Description                                                                               | Links                                                                                                                                           |
|--------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `color`            | `red`, `#DC143C`, `rgb(220,20,60)`                        | Set the color of text                                                                     | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/color), [w3schools](https://www.w3schools.com/cssref/pr_text_color.asp)                  |
| `font-family`      | `Arial`, `Helvetica`, `"Times New Roman"`                 | Set the font family, for custom fonts check out [Google Fonts](https://fonts.google.com/) | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family), [w3schools](https://www.w3schools.com/cssref/pr_font_font-family.asp)      |
| `font-size`        | `40px`, `10%`                                             | Set the font size                                                                         | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size), [w3schools](https://www.w3schools.com/cssref/pr_font_font-size.asp)          |
| `text-align`       | `left`, `center`, `right`                                 | Set the alignment of text                                                                 | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align), [w3schools](https://www.w3schools.com/cssref/pr_text_text-align.asp)        |
| `background-color` | `red`, `#DC143C`, `rgb(220,20,60)`                        | Set the background color of an element                                                    | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color), [w3schools](https://www.w3schools.com/cssref/pr_background-color.asp) |
| `background-image` | `url("image.jpg")`, `url("https://webite.com/image.jpg")` | Set the background image of an element                                                    | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image), [w3schools](https://www.w3schools.com/cssref/pr_background-image.asp) |
| `margin`           | `50px`, `5%`, `10px 0`                                    | Set the margin, the space between elements                                                | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/margin), [w3schools](https://www.w3schools.com/css/css_margin.asp)                       |
| `padding`          | `50px`, `5%`, `10px 0`                                    | Set the padding, the space inside an element                                              | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/padding), [w3schools](https://www.w3schools.com/css/css_padding.asp)                     |
| `border`           | `1px solid black`                                         | Set the border                                                                            | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/border), [w3schools](https://www.w3schools.com/css/css_border.asp)                       |
| `width`            | `100px`, `100%`                                           | Set the width of the element (only works on block elements)                               | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/width), [w3schools](https://www.w3schools.com/css/css_dimension.asp)                     |
| `height`           | `100px`, `100%`                                           | Set the height of the element (only works on block elements)                              | [mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/height), [w3schools](https://www.w3schools.com/css/css_dimension.asp)                    |

## CSS Lengths

You can read more about lengths in CSS [here](https://css-tricks.com/the-lengths-of-css/), [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Values_and_units), and [here](https://www.w3schools.com/cssref/css_units.asp). Keep in mind that in CSS a 'pixel' [isn't the same as a screen pixel](https://stackoverflow.com/questions/27382331/how-a-css-pixel-size-is-calculated).


| Unit | Relative To | Description |
|--- |--- |--- |
| px | absolute | pixels |
| cm | absolute | centimeters |
| mm | absolute | millimeters |
| in | absolute | inches |
| pt | absolute | point, 1pt == 1/72in |
| pc | absolute | pica, 1pc == 12pt |
| em | font | font size of the element, does not change with font family |
| rem | font | font size of root element (html), does not change with font family |
| ex | font | the height of "x", does change with font family |
| ch | font  | the width of "0", does change with font family |
| vw | viewport | 1vw == 1% of the width of the viewport |
| vh | viewport | 1vh == 1% of the height of the viewport |
| vmin | viewport | 1vmin == 1% of the viewport's smaller dimension |
| vmax | viewport | 1vmax == 1% of the viewport's larger dimension |
| %	 | parent | relative to the length of the parent's width or height |


## CSS Colors

RGB is short for [red green blue](https://en.wikipedia.org/wiki/RGB_color_model), with each value going from 0 to 255 (0 to FF in hexidecimal). Hexidecimal RGB values can also be specified with 3 values, in which case the digit is repeated (`#FFF` is the same as `#FFFFFF`).

HSL is short for [hue saturation lightness](https://en.wikipedia.org/wiki/HSL_and_HSV), with hue going from 0 to 360, and saturation and lightness going from 0% to 100%. The A stands for [alpha](https://en.wikipedia.org/wiki/Alpha_compositing), which goes from 0.0 to 1.0. You can learn more about CSS colors at the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value) and [w3schools](https://www.w3schools.com/cssref/css_colors.asp). You can view a nicely organized list of named colors [here](http://htmlcolorcodes.com/color-names/).

| color type | examples |
|--- |--- |
| RGB Hex | `#7FFFD4`, `#A9A9A9`, `#F00` |
| RGB Decimal | `rgb(127, 255, 212)` |
| RGBA Decimal | `rgba(255, 0, 0, 0.5)` |
| HSL | `hsl(120, 100%, 50%)` |
| HSLA | `hsla(120, 100%, 50%, 0.3)` |
| named color | `red`, `goldenrod`, `magenta` |


