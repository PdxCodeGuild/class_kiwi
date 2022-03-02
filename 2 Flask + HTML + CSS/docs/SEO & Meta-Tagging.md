# SEO & Meta-Tagging

SEO (search engine optimization) is an entire discipline of web development in itself.  Search engine optimizers specialize in bringing web pages to the top of results lists on search engines like Google, amongst other things.  

There is a lot that goes into SEO, but most things can be covered by adding `<meta>` tags to the `<head>` of the html file.  

The head contains metadata, which isn't displayed directly on the page, but serves as additional data about the document.  

Some elements in the head, like a `<link>` a css file, or a `<script>` tag, can ultimately change what appears on the page, but most `<meta>` tags don't, and the average web user has no idea they are there.  

Meta tags also determine how a preview will display when shared on Facebook or Slack:

![PDX Code Guild Link Slack Unfurl](slack-unfurl.png)

Moz.com has some good information about meta tags here (along with some templates for getting started): [https://moz.com/blog/meta-data-templates-123](https://moz.com/blog/meta-data-templates-123).  

You can learn about Open Graph here: [https://ogp.me](https://ogp.me).  

You can test your web page's social preview unfurls here: [https://www.opengraph.xyz/](https://www.opengraph.xyz/).  

Here is a template as well with some of the basics:
### Note: Any text in brackets will be completely replaced by text specific to your site (i.e.: `[https://example-website.com]`)
```html
<!DOCTYPE html>
<html lang="en">

<head>
	<!-- CHARSET AND VIEWPORT -->
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta http-equiv="X-UA-Compatible" content="ie=edge,chrome=1">

	<!-- LINKS -->
	<link rel="home" href="[https://your-domain-here.com/]">

	<!-- THEME COLOR -->
	<meta name="theme-color" content="[#32a914]">


	<title>[Your Title Here]</title>

	<!-- DESCRIPTION REFERRER ROBOTS -->
	<meta name="description" content="[Your Description Goes Here, This Is The Place Where SEOs Put Search Keywords]">
	<meta name="referrer" content="no-referrer-when-downgrade">
	<meta name="robots" content="all">
	<meta name="google-site-verification" content="[put your code here]" >

	<!-- OG, or Open Graph is Used by Many Crawlers to get Meta Data (facebook and others) -->
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="website" />
	<meta property="og:title" content="[This Can Be The Same As The Text In The <title> Element]">
	<meta property="og:description" content="[This Can Be The Same As The Text In The <meta name='description'> Tag]">

	<!-- Open Graph Image (Preview Image on Fb and others) -->
	<meta property="og:image" content="[https://your-website.com/preview-image.png]">
	<!-- following content values are dimensions of image in px -->
	<meta property="og:image:width" content="[1050]">
	<meta property="og:image:height" content="[630]">

	<meta property="og:see_also" content="[https://instagram.com/your-ig-name/]">
	<meta property="og:see_also" content="[https://www.linkedin.com/in/your-linked-in-url/]">
	<meta property="og:see_also" content="[https://twitter.com/your-twitter-handle/]">
	
	<!-- TWITTER -->
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="[@yourtwitterhandle]">
	<meta name="twitter:creator" content="[@yourtwitterhandle]">
	<meta name="twitter:title" content="[Title Text Here]">
	<meta name="twitter:description"
			content="[Description Text Here]">
	<!-- Twitter Preview Image -->
	<meta name="twitter:image" content="[https://your-website.com/preview-image.png]">
	<meta name="twitter:image:width" content="[1050]">
	<meta name="twitter:image:height" content="[630]">

	<!-- any other script or link tags you might need -->
</head>

<body>
<!-- content of body goes here -->
</body>

</html>
```

That covers the `<head>`, as for the `<body>`, the best thing you can do for SEO is to use semantic elements properly.  Here is a great article going in depth on why you should use semantic elements and how best to implement them: [https://www.semrush.com/blog/semantic-html5-guide/](https://www.semrush.com/blog/semantic-html5-guide/)