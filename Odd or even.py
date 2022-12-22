x = "Odd or even"
print(x.center(55))
print("")
num = int(input("Please enter a number: "))
print("")
if num%2 == 0:
  print("It is an even number.")
  print("")
else:
  print("")
  print("It is an odd number.")
print("")
print("yes(y) or no(n)")
print("")
retry = input("y or n: ")
while retry == "y":
  print("")
  num = int(input("Please enter a number: "))
  print("")
  if num%2 == 0:
    print("It is an even number.")
    print("")
  else:
    print("It is an odd number.")
    print("")
  retry = input("y/n: ")
while retry == "n":
  y = "--------------------------------------"
  print(y.center(55))
  z = "Thank you for trying out my program!"
  print(z.center(55))
  print(y.center(55))
  break
