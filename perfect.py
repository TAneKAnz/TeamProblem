def fah_to_cel(start, end, step):
    print(f"{'Fahrenheit':>12}{'Celcius':>12}")
    print(f"{'----------':>12}{'-------':>12}")
    if (start<end)and(step>0):
      fah = start
      while fah < end:
        cel = (5/9)*(fah-32)
        print(f"{fah:12.2f}{cel:12.2f}")
        fah = fah + step
    if (start>end)and(step<0):
      fah = start
      while fah > end:
        cel = (5/9)*(fah-32)
        print(f"{fah:12.2f}{cel:12.2f}")
        fah = fah + step
    print(f"{'----------':>12}{'-------':>12}")
