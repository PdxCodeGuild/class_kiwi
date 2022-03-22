
# Lab 3: URL Shortener

## Part 1

A url shortener is a web service that can take long urls (`https://www.google.com/search?source=hp&q=this+is+a+long+url&oq=this+is+a+long+url`) and create a short url (`goo.gl/pEc4vt`). Some examples are [bitly](https://bitly.com/), [TinyURL](https://tinyurl.com/), and [RB.GY](https://free-url-shortener.rb.gy/). These are used to put short, easily typed links onto flyers, twitter posts, etc.

When the short url is accessed, the view will take the code associated with that url (`pEc4vt`) and look up the url associated with it in the database. If that URL is found, it then redirects to that URL. You *could* use the ID in the url, instead of some code, but that then exposes some details about your database to the public.

Your app should contain the following:

- **Model**: a model `ShortenedURL` which has the following fields `code` (CharField), `url` (URLField) 
- **View 1** returns a page for entering in a url to be shortened, and a list of urls that have been shortened (`localhost:8000/shortener/`)
- **View 2** for receiving the form submission containing the long url, generating a random string, and saving it to the database (`localhost:8000/shortener/save/`)
- **View 3** performs the redirecting, which takes a `code` as a parameter (`localhost:8000/shortener/pEc4vt/`). Be sure to include the protocol ("https://") in the urls or redirecting will not work properly.



![url_shortener](django_url_shortener.png)



## Part 2

Add an IntegerField `counter` to the `ShortenedUrl` model, increment the counter every time the short url is accessed. Show the `counter` of each shortened url in the template.