x = ("Glen", "Sally", "Joseph")
print(x[2]) #Joseph

y = (1, 2, 3)
print(y) #(1, 2, 3)
print(max(y)) #3

for iter in y:
  print(iter)
  # 1
  # 2
  # 3


# Tuples and assigment
print("\nTuples and assigment")
(i,j) = (4, "Fred")
print(j) # Fred

(a,b) = (99, 98)
print(a) #99


# Tuples and dictionaries
print("\nTuples and assigment")
dictionary= {"chuck": 1, "fred": 42, "jan": 100}
tups = dictionary.items()
print(tups) # dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])


# Tuples are comparable
print("\nTuples are comparable")
(0, 1, 2) < (5, 1, 2) # True
(0, 1, 20000) < (0, 3, 4) # True
("Jones", "Sally") < ("Jones", "Sam") # True
("Jones", "Sally") > ("Adams", "Sam") # True


# Tuples are comparable
print("\nTuples are comparable")
d = {"a": 10, "d": 1, "c": 22}
d.items()
#dict_items([('a', 10), ('d', 1), ('c', 22)])
sorted(d.items())
#[('a', 10), ('c', 22), ('d', 1)]


# Using sorted()
print("\nUsing sorted()")
t = sorted(d.items())
print(t) # [('a', 10), ('c', 22), ('d', 1)]

for k,v in sorted(d.items()):
  print(k,v)
  # a 10
  # c 22
  # d 1


# Sort by values instead of keys
print("\nSort by values instead of keys")
tmp = list()

for k,v in d.items():
  tmp.append((v,k))

print(tmp) #[(10, 'a'), (1, 'd'), (22, 'c')]
tmp = sorted(tmp, reverse=True)
print(tmp) # [(22, 'c'), (10, 'a'), (1, 'd')]


# Shorter version for sorting
print("\nShorter version for sorting")
shorterSort = sorted([(v,k) for k,v in d.items()])
print(shorterSort)
