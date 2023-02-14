fileName= input("Enter file name: ")
wordsList= list()

try:
  file=open(fileName)

  for line in file:
    splitLine= line.split()

    for word in splitLine:
      if word not in wordsList:
        wordsList.append(word)
    
  wordsList.sort()
  print(wordsList)

except:
  print("Invalid file or folder")
  quit()