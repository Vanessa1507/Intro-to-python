isCorrectHour = False
isCorrectRate = False

#Try to parse the hours value to an int number, if not try it again
while isCorrectHour == False :
  try: 
    hours = input("Enter hours: ")
    hours= int(hours)
    isCorrectHour = True
  except:
    print('Error, "' + hours + '" is not a numeric value')
    isCorrectHour = False

#Try to parse the rate value to an float number, if not try it again
while isCorrectRate == False :
  try: 
    rate = input("Enter Rate: ")
    rate= float(rate)
    isCorrectRate = True
  except:
    print('Error, "' + rate + '" is not a numeric value')
    isCorrectRate = False

total = hours * rate
print(total)