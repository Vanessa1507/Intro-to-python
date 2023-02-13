isDone= False
numbers = []

while True :
  userInput = input("Enter a number: ", )
  try:
    if userInput != "done" :
      number= float(userInput)
      numbers.append(number)
    else:
      sum = 0
      for value in numbers: 
        sum = sum + value

      count = len(numbers)
      average = sum / count
      print(sum, count, average)
      break
  except:
    print("Invalid input")
