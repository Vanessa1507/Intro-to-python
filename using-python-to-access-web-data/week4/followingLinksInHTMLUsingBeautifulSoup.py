import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Lewin.html

def getHrefTag(url, position):
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, "html.parser")

  # Retrieve all anchor tags
  tags = soup("a")
  tag = tags[position - 1]
  link = tag.get("href")
  text = tag.get_text()
  return {"link": link, "text": text}

url = input("Enter URL - ")
if len(url) < 1:
  url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

position = input("Enter position: ")
try: position = int(position)
except: position = 3

count = input("Enter count: ")
try: count = int(count)
except: count = 4

link = getHrefTag(url, position)

name = ""
for i in range(count-1):
  link = getHrefTag(link["link"], position)

print(link["text"])