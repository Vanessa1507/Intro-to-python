import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# http://www.dr-chuck.com/page2.htm
url = input("Enter - ")
html = urllib.request.urlopen(url).read() # Read all
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
  print(tag.get("href", None))
