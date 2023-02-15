purse = dict()
purse["money"] = 12
purse["candy"] = 13
purse["tissues"] = 75
print(purse) #{'money': 12, 'candy': 12, 'tissues': 75}
print(purse["candy"]) #13

purse["candy"] = purse["candy"] + 13
print(purse["candy"]) #2


print("\nExample2")
counts = dict()
names=["csev", "cwen", "zqian", "cwen"]
for name in names:
  if name not in counts:
    counts[name]= 1
  else:
    counts[name]= counts[name]+1
print(counts)


#get
print("\nget method")
counts2= dict()
for name in names:
  counts2[name]= counts2.get(name, 0) + 1
print(counts2)

#For loop
print("\nFor loop")
counts3= {"chuck": 1, "fred": 42, "jan": 100}
for key in counts3:
  print(key, counts3[key])


#Retrieving lists of keys and values
print("\nRetrieving lists of keys and values")
print(list(counts3)) # ['chuck', 'fred', 'jan']
print(counts3.keys()) # dict_keys(['chuck', 'fred', 'jan'])
print(counts3.values()) # dict_values([1, 42, 100])
print(counts3.items()) # dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])


# Two iteration variables
print("\nTwo iteration variables")
for key,value in counts3.items():
  print(key,value)
  #chuck 1
  #fred 42
  #jan 100