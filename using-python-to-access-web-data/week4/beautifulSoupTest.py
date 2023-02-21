import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# http://www.dr-chuck.com/page2.htm
url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read() # Read all
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
  print(tag.get("href", None))
