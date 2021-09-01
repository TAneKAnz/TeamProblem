x = input("Enter a number (or [Enter] to exit): ")
if x == "" :
  print("Nothing to do.")
else :
  max = float(x)
  min = float(x)
  sum = 0
  i = 0
  while not x == "" :
    x = float(x)
    i += 1
    sum += x
    if x > max :
      max = x
    if x < min :
      min = x
    x = input("Enter a number (or [Enter] to exit): ")
  average = sum / i
  print("Maximum value is ", format(max,".2f"))
  print("Minimum value is ", format(min,".2f"))
  print("Average value is ", format(average,".2f"))