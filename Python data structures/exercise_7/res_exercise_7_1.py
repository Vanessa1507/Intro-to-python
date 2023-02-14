file = open("./mbox-short.txt")

for line in file :
  newLine = line.rstrip()
  print(newLine.upper())

abc = "First; Second; Third"
split = abc.split("; ")
print(split) #['with', 'three', 'words']