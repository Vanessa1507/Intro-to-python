import re
file = open("../../txt/mbox-short.txt")


print("re.search() like find()")
# for line in file:
#   line = line.rstrip()
#   if line.find("From:") >= 0:
#     print(line)

# Regular expressions
# for lineRe in file:
#   lineRe = lineRe.rstrip()
#   if re.search("From:", lineRe) :
#     print(lineRe)

print("\nre.search() like startswith()")
for line in file:
  line = line.rstrip()
  if line.startswith("From:"):
    print("startswith", line)

# Regular expressions
for lineSw in file:
  lineSw = lineSw.rstrip()
  if re.search("^From:", lineSw) :
    print("search()",lineSw)


# Matching and extracting data
print("\nMatching and extracting data")
x = "My 2 favorite numbers are 19 and 42"
y1 = re.findall("[0-9]+", x)
y2 = re.findall("[AEIOU]+", x)
print(y1) # ['2', '19', '42']
print(y2) # []


# Greedy matching
print("\nGreedy matching")
text = "From: Using the : character"
greedyMatch = re.findall("^F.+:", text)
print(greedyMatch) # From: Using the :


# Non-Greedy matching
print("\nNon-Greedy matching")
text2 = "From: Using the : character"
nonGreedyMatch = re.findall("^F.+?:", text2)
print(nonGreedyMatch) # From:


# Fine-Tuning String Extraction
print("\nFine-Tuning String Extraction")
fromText = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
email = re.findall("\S+@\S+", fromText)
print(email) # ['stephen.marquard@uct.ac.za']
email2 = re.findall("^From (\S+@\S+)", fromText)
print(email2) # ['stephen.marquard@uct.ac.za']


# Extract a host from a email
print("\nExtract a host from a email")
host = re.findall("@([^ ]*)", fromText)
print(host) # ['uct.ac.za']


# Even cooler regex version
print("\nEven cooler regex version")
host2 = re.findall("^From .*@([^ ]*)", fromText)
print(host2) # ['uct.ac.za']


# Escape character
print("\nEscape character")
text3 = "We just received $10.00 for cookies."
number = re.findall("\$[0-9.]+", text3)
print(number) # ['$10.00']
