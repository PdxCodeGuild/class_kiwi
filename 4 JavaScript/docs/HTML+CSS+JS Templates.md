

# HTML+CSS+JS Templates


- [Vanilla JS](#vanilla-js)
  - [Vanilla CSS](#vanilla-css)
  - [Materialize](#materialize)
  - [Bootstrap](#bootstrap)
- [Vue](#vue)
  - [Vanilla CSS](#vanilla-css-1)
  - [Materialize](#materialize-1)
  - [Bootstrap](#bootstrap-1)
- [Vue + Axios](#vue--axios)
  - [Vanilla CSS](#vanilla-css-2)
  - [Materialize](#materialize-2)
  - [Bootstrap](#bootstrap-2)



## Vanilla JS

### Vanilla CSS

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World!</title>
    <!-- Page CSS -->
    <style type="text/css">
        #title {
            color: blue;
        }
    </style>
</head>
    <body>
        <!-- Page Content -->
        <h1 id="title">Hello World!</h1>
        <!-- Page JS -->
        <script type="text/javascript">
            let h1 = document.querySelector('#title')
            h1.innerText += '!'
        </script>
    </body>
</html>
```


### Materialize

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World!</title>
    <!-- Materialize CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
</head>
    <body>
        <h1 id="title">Hello World!</h1>
        <!-- Materialize JS -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        <!-- Page JS -->
        <script type="text/javascript">
            // initialize Materialize components
            M.AutoInit()

            let h1 = document.querySelector('#title')
            h1.innerText += '!'
        </script>
    </body>
</html>
```

### Bootstrap

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Hello World!</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    </head>
    <body>
        <h1 id="title">Hello World!</h1>
        <!-- Bootstrap JS -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
        <!-- Page JS -->
        <script type="text/javascript">
            let h1 = document.querySelector('#title')
            h1.innerText += '!'
        </script>
    </body>
</html>
```

## Vue



### Vanilla CSS

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World!</title>
    <!-- Page CSS -->
    <style type="text/css">
        #app h1 {
            color: blue;
        }
    </style>
</head>
    <body>
        <!-- Page Content -->
        <div id="app">
            <h1>{{ title }}</h1>
        </div>
        <!-- Vue JS -->
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
        <!-- Page JS -->
        <script type="text/javascript">
            let app = new Vue({
                el: '#app',
                data: {
                    title: 'Hello World!'
                }
            })
        </script>
    </body>
</html>
```


### Materialize

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World!</title>
    <!-- Materialize CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
</head>
    <body>
        <!-- Page Content -->
        <div id="app">
            <h1>{{ title }}</h1>
        </div>
        <!-- Materialize JS -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        <!-- Vue JS -->
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
        <script type="text/javascript">
            // initialize Materialize components
            M.AutoInit()
            
            let app = new Vue({
                el: '#app',
                data: {
                    title: 'Hello World!'
                }
            })
        </script>
    </body>
</html>
```

### Bootstrap

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Hello World!</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    </head>
    <body>
        <!-- Page Content -->
        <div id="app">
            <h1>{{ title }}</h1>
        </div>
        <!-- Bootstrap JS -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
        <!-- Vue JS -->
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
        <!-- Page JS -->
        <script type="text/javascript">
            let app = new Vue({
                el: '#app',
                data: {
                    title: 'Hello World!'
                }
            })
        </script>
    </body>
</html>
```


## Vue + Axios


### Vanilla CSS

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World!</title>
    <!-- Page CSS -->
    <style type="text/css">
        #app h1 {
            color: blue;
        }
    </style>
</head>
    <body>
        <!-- Page Content -->
        <div id="app">
            <h1>{{ title }}</h1>
        </div>
        <!-- Vue JS -->
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
        <!-- Axios JS -->
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <!-- Page JS -->
        <script type="text/javascript">
            let app = new Vue({
                el: '#app',
                data: {
                    title: 'Hello World!'
                },
                created: function() {
                    axios({
                        method: 'get',
                        url: 'https://api.ipify.org/',
                        params: {
                            format: 'json'
                        }
                    }).then(response => {
                        console.log(response.data)
                        this.title = response.data.ip
                    })
                }
            })
        </script>
    </body>
</html>
```


### Materialize

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World!</title>
    <!-- Materialize CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
</head>
    <body>
        <!-- Page Content -->
        <div id="app">
            <h1>{{ title }}</h1>
        </div>
        <!-- Materialize JS -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        <!-- Vue JS -->
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
        <!-- Axios JS -->
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <!-- Page JS -->
        <script type="text/javascript">
            // initialize Materialize components
            M.AutoInit()
            
            let app = new Vue({
                el: '#app',
                data: {
                    title: 'Hello World!'
                },
                created: function() {
                    axios({
                        method: 'get',
                        url: 'https://api.ipify.org/',
                        params: {
                            format: 'json'
                        }
                    }).then(response => {
                        console.log(response.data)
                        this.title = response.data.ip
                    })
                }
            })
        </script>
    </body>
</html>
```

### Bootstrap

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Hello World!</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    </head>
    <body>
        <!-- Page Content -->
        <div id="app">
            <h1>{{ title }}</h1>
        </div>
        <!-- Bootstrap JS -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
        <!-- Vue JS -->
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
        <!-- Axios JS -->
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <!-- Page JS -->
        <script type="text/javascript">
            let app = new Vue({
                el: '#app',
                data: {
                    title: 'Hello World!'
                },
                created: function() {
                    axios({
                        method: 'get',
                        url: 'https://api.ipify.org/',
                        params: {
                            format: 'json'
                        }
                    }).then(response => {
                        console.log(response.data)
                        this.title = response.data.ip
                    })
                }
            })
        </script>
    </body>
</html>
```
