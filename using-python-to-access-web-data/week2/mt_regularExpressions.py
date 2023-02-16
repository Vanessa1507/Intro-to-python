import re

fileName = input("Enter the file name: ")

if len(fileName) < 1:
  fileName = "regex_sum_1754012.txt"

numList = list()

try:
  file = open("../../txt/"+fileName)
  for line in file :
    numInLine = re.findall("[0-9]+", line)
    if len(numInLine) < 1 : continue

    for num in numInLine:
      numList.append(int(num))
  
  numsSum = str(sum(numList))
  print("There are", len(numList), "values and the sum ends with", numsSum[len(numsSum)-3:])
except:
  print("There is no a valid file")
  quit()
