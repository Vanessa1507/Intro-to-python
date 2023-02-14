#Create a list
newList = list()
newList.append(2)
newList.append(3)
newList.append(4)
print(newList) # [2,3,4]

#Concat
a = [1,2,3]
b = [4,5,6]
c = a + b # [1,2,3,4,5,6]

#Slice
sliceList = [1,2,3,4,5,6]
sliceList[1:3] #[2,3]


#Split
abc = "with three words"
split = abc.split()
print(split) #['with', 'three', 'words']

abc2 = "First; Second; Third"
split2 = abc2.split("; ")
print(split) #['First', 'Second', 'Third']

#Sort
newList = ["Maria", "Laura", "Ivan"]
newList.sort() #["Ivan", "Laura", "Maria"]

#Check
checkList = [1,2,3,4,5,6]
9 in checkList # False
13 not in checkList # True

#Len
numbers = [1,2,3,4,5]
length= len(numbers) #Value= 5

#Range
range(4) #returns [0,1,2,3]
