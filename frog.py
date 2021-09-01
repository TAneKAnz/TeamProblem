h = int(input("Enter the depth of the well: "))
u = int(input("Enter the height the frog can jump up: "))
d = int(input("Enter the height the frog slips down: "))
i = 1
if d >= u :
  print("The frog is always stuck in the well.")
else:
  while  h > u :
    i += 1
    h -= u
    print("On day {0} the frog leaps to the depth of {1} meters.".format(i, h))
    h += d
    print("At night he slips down to the depth of {0} meters.".format(h))
  print("The frog is free on day {0}.".format(i))