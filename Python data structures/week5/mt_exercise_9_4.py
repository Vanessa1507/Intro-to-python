fileName = input("Enter file:")
if len(fileName) < 1:
  fileName = "mbox-short.txt"

dictionary = dict()
emails = list()
try:
  file = open("../../txt/" + fileName)
  
  for line in file:
    line = line.rstrip()
    if not line.startswith("From "):
      continue

    words = line.split()
    emails.append(words[1])
  
  for email in emails:
    dictionary[email] = dictionary.get(email, 0) + 1

  mostSender = ""
  numEmailsSent = None
  for key,value in dictionary.items():
    if numEmailsSent == None or value > numEmailsSent:
      mostSender = key
      numEmailsSent = value
  
  print(mostSender, numEmailsSent)

except:
  print("There is no a valid file")
  quit()


