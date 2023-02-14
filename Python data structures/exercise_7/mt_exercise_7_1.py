try :
  file = open("../../txt/mbox-short.txt")

  for line in file :
    uppercase = line.upper()
    print(uppercase)
except:
  print("There is no file")
  quit()