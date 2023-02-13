hoursInput = input("Enter hours: ")
rateInput = input("Enter Rate: ")

try:
  hours = int(hoursInput)
  rate = float(rateInput)
except:
  print("Error, please enter numeric value")
  quit()

if hours > 40 :
  regular = hours * rate
  overtime= (hours - 40) * (rate * 0.5)
  total = regular + overtime
else:
  total =  hours * rate

print("Pay:", total)