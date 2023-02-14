emails = list()

try:
  fileName = input("Enter file name: ")

  if len(fileName) < 1:
    fileName = "mbox-short.txt"

  file = open("../../txt/" + fileName)

  for line in file :
    if line.startswith("From ") : 
      splitLine = line.split()
      email = splitLine[1]
      emails.append(email)
      print(email)
  print("There were", len(emails), "lines in the file with From as the first word")
except:
  print("There is not file")
  quit()