import urllib.request

fileHandle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in fileHandle:
  print(line.decode().strip())