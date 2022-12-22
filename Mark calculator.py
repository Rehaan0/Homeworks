print("-----------------")
x = "PT-3 MARKS"
print(x.center(12))
print("-----------------")

print("SUBJECT | MARKS  ")
print("-----------------")
ai=float(input("AI      |   "))
while ai>20:
  print("The maximum marks is 20,please try again.")
  ai=float(input("AI      |   "))
print("-----------------")
english = float(input("English |   "))
while english>40:
  print("The maximum marks is 40, please try again.")
  english = float(input("English |   "))
print("-----------------")
science = float(input("Science |   "))
while science> 40:
  print("The maximum marks is 40, please try again.")
  science = float(input("Science |   "))
print("-----------------")
social = float(input("Social  |   "))
while social> 40:
  print("The maximum marks is 40, please try again.")
  social = float(input("Social  |   "))
print("-----------------")
tamil = float(input("Tamil   |   "))
while tamil > 40:
  print("The maximum marks is 40, please try again.")
  tamil = float(input("Tamil   |   "))
print("-----------------")
hindi = float(input("Hindi   |   "))
while hindi > 20:
  print("The maximum marks is 20, please try again")
  hindi = float(input("Hindi   |   "))
print("-----------------")
maths = float(input("Maths   |   "))
while maths > 40:
  print("The maximum marks is 40, please try again.")
  maths = float(input("Maths   |  "))
print("-----------------")
print("TOTAL   |  ", maths + hindi + tamil + social + science + english + ai)
print("-----------------")

ai1 = ai/20 * 100
hindi1 = hindi/20 * 100
ai2 = ai1/100 * 40
hindi2 = hindi1/100 * 40

x = (ai2 + english + science + social + tamil + hindi2 + maths) / 7
y = round(x,2)
print("AVERAGE |  ", y)
print("-----------------")
