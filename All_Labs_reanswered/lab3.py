# absolute value
num = float(input("Insert any number: "))
if num < 0:
  num = -1 * num
print("Absolute value of this num is", num)


# min value:
num1 = float(input("Insert first number: "))
num2 = float(input("Insert second number: "))
num3 = float(input("Insert third number: "))
min_num = 0
if num1 <= num2:
  if num1 <= num3:
    min_num = num1
  else:
    min_num = num3
else:
  if num2 <= num3:
    min_num = num2
  else:
    min_num = num3
print("Minumum number is: ", min_num)

# GPA/ num_of_courses

GPA = float(input("Insert GPA: "))
num_of_courses = int(input("Insert number of courses: "))

if GPA < 2 and num_of_courses < 47:
  print("Not enough courses or GPA")
elif num_of_courses < 47:
  print("Not enough number of lectures")
elif GPA < 2:
  print("Not enough GPA")
else:
  print("Graduated!")

# Ticket discount:
ticket_price = 3
discount = 0.5
age = int(input("Insert your age: "))
if age < 6 or age > 60:
  ticket_price = 0
elif age<=18:
  ticket_price = ticket_price * (1-discount)

print("Your ticket price is: ", ticket_price)

# Roots of quadratic had a similar solution in lab 2
# Seasons question requires a long if-else statement so I did not resolve it.


