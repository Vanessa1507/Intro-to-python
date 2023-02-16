# Top 10 most common words

fhand = open("../../txt/romeo.txt")
counts = dict()

for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1

# lst = list()
# for key, val in counts.items():
#   newtup = (val, key)
#   lst.append(newtup)

# lst = sorted(lst, reverse= True)

# for val, key in lst[:10]:
#   print(key, val)

top10 = sorted([(v,k) for k,v in counts.items()], reverse=True)[:10]
print(top10)

for v,k in top10:
  print(k, v)