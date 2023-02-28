import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL - ")

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml
#Actual data: http://py4e-data.dr-chuck.net/comments_1754016.xml

if len(url) < 1:
  url= "http://py4e-data.dr-chuck.net/comments_42.xml"

fileHandle = urllib.request.urlopen(url).read()

tree = ET.fromstring(fileHandle)

numList = list()

# countList=tree.findall("comments/comment")
# for item in countList:
#   num = item.find("count").text
#   numList.append(int(num))

countList=tree.findall(".//count")
for item in countList:
  num = item.text
  numList.append(int(num))


print(sum(numList))