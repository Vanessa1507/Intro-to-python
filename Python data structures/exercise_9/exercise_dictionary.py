fname = input("Enter file:")
if len(fname) < 1: fname = "clown.txt"

hand = open("../../txt/" + fname)

di = dict()
for lin in hand:
  lin = lin.rstrip()
  wds = lin.split()

  for w in wds:
    #idiom: retrieve/create/update counter
    di[w]= di.get(w, 0) + 1
    # print(w)

# print(di)

largest = -1
theWord = None
#Now we want to find the most common word
for k,v in di.items():
  if v > largest :
    largest = v
    theWord = k #capture/remember the word that was largest

print("Done", theWord, largest)