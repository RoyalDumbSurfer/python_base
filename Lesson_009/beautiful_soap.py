from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# relative all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
