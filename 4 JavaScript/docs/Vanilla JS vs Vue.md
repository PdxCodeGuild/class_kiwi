

# Vanilla JS vs Vue

- [Setting Inner Text](#setting-inner-text)
- [Setting Inner HTML](#setting-inner-html)
- [Setting Attributes](#setting-attributes)
- [Handling Events](#handling-events)
- [Getting Input](#getting-input)
- [Generating Elements](#generating-elements)


## Setting Inner Text

Both of these result in `<div>hello world!</div>`

**Vanilla**
```html
<div id="mydiv"></div>
<script>
    let mydiv = document.querySelector('#mydiv')
    mydiv.innerText = 'hello world!'
</script>
```

**Vue**
```html
<div id="app">
    <div>{{message}}</div>
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

## Setting Inner HTML

Both of these result in `<div><b>hello world!</b></div>`

**Vanilla**
```html
<div id="mydiv"></div>
<script>
    let mydiv = document.querySelector('#mydiv')
    mydiv.innerHTML = '<b>hello world!</b>'
</script>
```

**Vue**
```html
<div id="app">
    <div v-html="message"></div>
</div>
<script>
    let app = new Vue({
        el: '#app',
        data: {
            message: '<b>hello world!</b>'
        }
    })
</script>
```

## Setting Attributes

Both of these result in `<div title="hello world!">hover over me</div>`


**Vanilla**
```html
<div id="mydiv">hover over me</div>
<script>
    let mydiv = document.querySelector('#mydiv')
    mydiv.setAttribute('title', 'hello world!')
</script>
```

**Vue**
```html
<div id="app">
    <div v-bind:title="message">hover over me</div>
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


## Handling Events

Both these result in a button that alerts 'hello world!'.

**Vanilla**
```html
<button id="mybutton">click</button>
<script>
    let mybutton = document.querySelector('#mybutton')
    mybutton.addEventListener('click', function() {
        alert('hello world!')
    })
</script>
```

**Vue**
```html
<div id="app">
    <button v-on:click="sayHello">click</button>
</div>
<script>
    let app = new Vue({
        el: '#app',
        methods: {
            sayHello: function() {
                alert('hello world!')
            }
        }
    })
</script>
```

## Getting Input

Both these result in a button that alerts whatever text typed into the text field.

**Vanilla**
```html
<input id="myinput" type="text"/>
<button id="mybutton">click</button>
<script>
    let mybutton = document.querySelector('#mybutton')
    let myinput = document.querySelector('#myinput')
    mybutton.addEventListener('click', function() {
        alert(myinput.value)
    })
</script>
```

**Vue**
```html
<div id="app">
    <input type="text" v-model="message"/>
    <button v-on:click="sayHello">click</button>
</div>
<script>
    let app = new Vue({
        el: '#app',
        data: {
            message: 'hello world!'
        },
        methods: {
            sayHello: function() {
                alert(this.message)
            }
        }
    })
</script>
```

## Generating Elements


**Vanilla**
```html
<ul id="mylist"></ul>
<script>
    let mylist = document.querySelector('#mylist')
    let fruits = ['apples', 'bananas', 'pears']
    for (let i=0; i<fruits.length; ++i) {
        let li = document.createElement('li')
        li.innerText = fruits[i]
        mylist.appendChild(li)
    }
</script>
```

**Vue**
```html
<div id="app">
    <ul>
        <li v-for="fruit in fruits">{{fruit}}</li>
    </ul>
</div>
<script>
    let app = new Vue({
        el: '#app',
        data: {
            fruits: ['apples', 'bananas', 'pears']
        }
    })
</script>
```
