x = int(input("enter a value: "))
if x < 0:
  print(-x)
else:
  print(x)

y = float(input("enter a value1: "))
z = float(input("enter a value2: "))
c = float(input("enter a value3: "))
if c <= y:
  if c<=z:
    z=11
  else:
    c=11
else:
  if y<=z:
    y=11
  else:
    z=11


gpa=float(input("enter GPA"))
num_of_lec= float(input("enter number of lectures"))
if gpa<2:
  if num_of_lec >= 47:
    print("not enough gpa")
  else:
    print("not enough gpa or lectures")
else:
  if num_of_lec< 47:
    print("not enough lectures")
  else:
    print("graduated")

def excer3():
  age= int(input("insert an age"))
  ticket = 3
  if age < 6 or age > 60:
    ticket = 0
  elif age >= 6 and age <=18:
    ticket= 0.5* ticket
  else:
    ticket= ticket *1
  return ticket

print(excer3())