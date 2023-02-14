file = open("./mbox-short.txt")

for line in file :
  newLine = line.rstrip()
  print(newLine.upper())