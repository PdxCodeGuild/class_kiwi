from urllib import request
import json

response = request.urlopen("https://www.gutenberg.org/files/67325/67325-h/67325-h.htm")
data = json.loads(response.read())

print(data)
# raw = response.read()
