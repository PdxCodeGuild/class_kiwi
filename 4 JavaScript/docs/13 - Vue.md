

# Vue


- [Overview](#overview)
- [Including Vue](#including-vue)
- [Anatomy of a Vue App](#anatomy-of-a-vue-app)
- [Rendering Values](#rendering-values)
- [Setting Attributes](#setting-attributes)
- [Conditionals](#conditionals)
- [Loops](#loops)
- [Input Fields](#input-fields)
- [Event Listeners](#event-listeners)
- [Lifecycle Hooks](#lifecycle-hooks)

## Overview

Front-end frameworks like **Vue**, **React** (Facebook), and **Angular** (Google) can be used to create complex, interactive web pages. The principle advantage they offer is the separation of *display* and *data*. Developing complex pages in [vanilla JavaScript](http://vanilla-js.com/) becomes cumbersome and messy, every time an value is updated, certain HTML elements must be created or hidden, have its style changed, have its inner text changed, etc. Libraries like **Vue.js** allows  the HTML section to decide how things are displayed and allows the JavaScript section to decide how data is processed.


- [Vue](https://vuejs.org/)
- [Intro to Vue](https://vuejs.org/v2/guide/index.html)
- [Cheat Sheet](https://www.vuemastery.com/pdf/Vue-Essentials-Cheat-Sheet.pdf)

You may also want to install the [Vue.js devtools](https://github.com/vuejs/vue-devtools) for [chrome](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=en) and [firefox](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/).

## Including Vue

You can include Vue in your page like so:

```html
<!-- development version, includes helpful console warnings -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<!-- or -->

<!-- production version, optimized for size and speed -->
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
```



## Anatomy of a Vue App


```html
<!-- html element represnting the app, referenced by 'el' -->
<div id="app">
  <!-- display 'message' from the 'data' part of the app in the page -->
  <span>{{ message }}</span>
  <!-- allow the user to set the value of the input -->
  <input type="text" v-model="message"/>
  <!-- handle a click event of a button - calls the method sayHello -->
  <button v-on:click="sayHello">click</button>
</div>
<script>
  let app = new Vue({
    // query selector of the html element representing the app
    el: '#app',
    // app data
    // data stored with the app
    // for displaying in the page: {{message}}
    // for getting input from the user: v-model="message"
    // for modifying in methods: this.message
    data: {
      message: 'hello world!'
    },
    // app methods
    // can be called from events in the page: v-on:click="method"
    // can be called from other methods: this.method()
    // can be called from outside the app: app.method()
    methods: {
      sayHello: function() {
        console.log(this.message)
      }
    },
    // created - a lifecycle hook
    // called when the app is created
    // useful for setting up app data
    created: function() {
      console.log(this.message)
    }
  })
</script>
```



## Rendering Values

Render variables in the HTML using `{{}}`. [more info](https://vuejs.org/v2/guide/syntax.html#Interpolations)

```html
<div id="app">
  <span>{{ message }}</span>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      message: 'hello world!'
    }
  })
</script>
```

## Setting Attributes

Set attribute values using `v-bind`. [more info](https://vuejs.org/v2/guide/syntax.html#Attributes)

```html
<div id="app">
  <img v-bind:src="image_url"/>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      image_url: 'https://placekitten.com/200/200'
    }
  })
</script>
```

If the value of the variable is falsey, the attribute won't be added to the element at all, which is useful for attributes like `disabled`, `checked`, etc.

```html
<div id="app">
  <input type="checkbox" v-model="disable_button"> disable button<br/>
  <button v-bind:disabled="disable_button">click</button>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      disable_button: false
    }
  })
</script>
```

## Conditionals


There are two directive for controlling the visibility of an HTML element, `v-if` and `v-show`. If the variable they're associated with is `true`, the element will be shown, if it is `false`, it won't be. `v-if` actually removes the element, while `v-show` simply hides it. `v-if` has a higher toggle cost, but `v-show` has a higher initial cost (if the value is initially `false`). [more info](https://vuejs.org/v2/guide/conditional.html)

```html
<div id="app">
  <span v-if="seen">some text</span>
  <span v-show="seen">some text</span>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      seen: true
    }
  })
</script>
```

## Loops

Loop over a list using `v-for`, repeatedly generating elements. Just like with Python, the variable name is arbitrary. You can optionally add an index. [more info](https://vuejs.org/v2/guide/list.html)

```html
<div id="app">
  <ul>
    <li v-for="color in colors">{{ color }}</li>
  </ul>
  <ul>
    <li v-for="(color, index) in colors">{{ index }}) {{ color }}</li>
  </ul>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      colors: ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    }
  })
</script>
```

## Input Fields

You can bind app variables to input fields using `v-model`. If the user changes the value of the input field, the variable in the app will be updated and vice versa. [more info](https://vuejs.org/v2/guide/forms.html)


```html
<div id="app">
  <input type="text" v-model="name"/>
  <select v-model="color">
    <option value="red">red</option>
    <option value="green">green</option>
    <option value="blue">blue</option>
  </select>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {
      name: 'bob',
      color: 'red',
    }
  })
</script>
```

## Event Listeners

Bind events on elements to methods using `v-on`. [list of event types](12%20-%20Events.md#list-of-events) [more info](https://vuejs.org/v2/guide/events.html)

```html
<div id="app">
  <button v-on:click="doSomething">click</button>
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {},
    methods: {
      doSomething: function() {
        alert('clicked!')
      }
    }
  })
</script>
```


## Lifecycle Hooks

Lifecycle hooks are special functions called throughout the lifecycle of a Vue app, `created` is called when an app is created, `mounted` is called when an app is mounted, etc. These are useful if you want to generate app data or load it from an api. [more info](https://vuejs.org/v2/guide/instance.html#Instance-Lifecycle-Hooks)

```html
<div id="app">
</div>
<script>
  let app = new Vue({
    el: '#app',
    data: {},
    created: function() {
      alert('app created!')
    }
  })
</script>
```