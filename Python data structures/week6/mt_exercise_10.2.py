fileName = input("Enter file:")
if len(fileName) < 1:
    fileName = "mbox-short.txt"

dictionary = dict()
timeList = list()
try:
  file = open("../../txt/" + fileName)
  for line in file:
    line = line.rstrip()

    if not line.startswith("From "):
      continue

    words = line.split()
    timeList.append(words[5].split(":")[0])
    
  for time in timeList:
    dictionary[time] = dictionary.get(time, 0) + 1
  
  sortTime = sorted(dictionary.items())
  # print(sortTime)

  for key, value in sortTime:
    print(key, value)

except:
  print("There is no valid file")
  quit()
