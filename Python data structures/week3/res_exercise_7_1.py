file = open("../../txt/mbox-short.txt")

for line in file :
  newLine = line.rstrip()
  print(newLine.upper())