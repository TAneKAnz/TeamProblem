x = float(input("Enter a number (or zero to exit): "))
sump = 0
sumn = 0
while not x == 0 :
  if x > 0 :
    sump += x
  else :
    sumn += x
  x = float(input("Enter a number (or zero to exit): "))
print("Sum of positive number is ", format(sump,".2f"))
print("Sum of negative number is ", format(sumn,".2f"))