han = open("../../txt/mbox-short.txt")

for line in han:
  line = line.rstrip()
  wds = line.split()

  #Guardian
  if len(wds) < 3 or wds[0] != "From": 
    continue
  print(wds[1])