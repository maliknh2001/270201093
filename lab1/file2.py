x = int(input("enter a value: "))
if x < 0:
  print(-x)
else:
  print(x)
 
def excer1 ():
  y = float(input("enter a value1: "))
  z = float(input("enter a value2: "))
  c = float(input("enter a value3: "))
  if c <= y:
    if c<=z:
      l1=c
    else:
      l1=z
  else:
    if y<=z:
      l1=y
    else:
      l1=z
  return l1

def excer2():
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