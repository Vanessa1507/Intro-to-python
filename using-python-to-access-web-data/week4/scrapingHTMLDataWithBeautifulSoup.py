import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1754014.html (Sum ends with 52)
url = input("Enter - ")
if len(url) < 1:
  url = "http://py4e-data.dr-chuck.net/comments_42.html"

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup("span")
numList= list()

for tag in tags:
  num = int(tag.get_text())
  if type(num) != "str":
    numList.append(num)

print(sum(numList))