import urllib.request, urllib.parse
import json

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1754017.json (Sum ends with 12)

url = input("Enter URL - ")

if len(url) < 1:
  url = "http://py4e-data.dr-chuck.net/comments_1754017.json"

data= urllib.request.urlopen(url).read()

info = json.loads(data)

comments = info["comments"]

countList = list()
for comment in comments:
  countList.append(int(comment["count"]))

print(sum(countList))