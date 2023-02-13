num = 0
total= 0.0

while True :
  inputValue = input("Enter a number: ")

  if inputValue == "done" :
    break
  try: 
    value = float(inputValue)
  except :
    print("Invalid input")
    continue
  
  num = num + 1
  total = total + value

print (total, num, total/num)