import requests

url="http://www.python.org"

# making get() request on above url
response=requests.get(url)
print(response.status_code)

# print content of page ,content is of byte type so we need to decode in string
print(response.content.decode())


from bs4 import BeautifulSoup
 
## The HTML Data can be fetched using requests or can be a variable (a multiline string)
## If fetching with requests
# import requests
# response = requests.get('https://www.python.org')
# soup = BeautifulSoup(response.content, 'html.parser')
 
 
html = '''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
   <title>My title</title>
</head>
<body>
This is just a text <br />
<p class='css1'>first paragraph </p>
<p id='myid'>second paragraph </p>
<p>third paragraph </p>
<br />
<a href="https://www.python.org" class='mylink'>first link</a><br />
<a href="http://www.linux.com">second link</a>
<br />
<div class='some_class'>
   this is inside a div<br />
   <p>paragraph inside a div</p>
</div>
</body>
</html>
'''
 
## Creating a soup object
soup = BeautifulSoup(html, 'html.parser')
 
# Get  title tag
print(soup.title)
 
## Get first div of the body
d = soup.body.div
 
print(type(d)) 
 
## Finding ALL <p> tags, it returns a list
print(soup.find_all('p'))
 
## Finding and printing the content of all <div> tags
print(soup.find('div').text)
 
## Finding all <p> tags, iterating over the returned list and getting the content of each <p> tag
for x in soup.find_all('p'):
    print(x.text)
 
 
## Finding all <div> and <p> tags
print(soup.find_all(['div', 'p']))
 
## Finding all <p> tags that have id='myid'
print(soup.find_all('p', id='myid'))
 
## Finding all <div> tags that have class='some_class'
print(soup.find_all('div', class_='some_class'))
 
## Finding and printing all links
links = soup.find_all('a', href=True)
print(links)
 
for link in links:
    print(link.get('href'))
