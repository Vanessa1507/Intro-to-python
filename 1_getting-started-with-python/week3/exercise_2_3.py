hoursInput = input("Enter hours: ")
rateInput = input("Enter Rate: ")
hours = int(hoursInput)
rate = float(rateInput)

if hours > 40 :
  regular = hours * rate
  overtime= (hours - 40) * (rate * 0.5)
  total = regular + overtime
else:
  total =  hours * rate

print("Pay:", total)