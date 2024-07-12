yr = int(input("Enter year to check : "))

if yr % 4 == 0:
  if yr % 100 == 0:
    if yr % 400 == 0:
      print(f"{yr} is Leap Year ")
    else:
      print(f"{yr} Not Leap Year ")
  else:
    print(f"{yr} is Leap Year ")
else:
  print(f"{yr} Not Leap Year ")
  
    