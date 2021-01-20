# Sum of last 2 
num = input("Insert any number that is at least 2 digits: ")
summation = int(num[-1]) + int(num[-2])
print("Sum of last 2 digits: ", summation)

# Leap year:
year = input("Insert a year:")
leap_year= False
century_year = False
if len(year) > 2:
  if year[-1] == "0" and year[-2] == "0":
    century_year = True

if century_year:
  if int(year) % 400 == 0:
    leap_year = True
  else:
    leap_year = False
else:
  if int(year) % 4 == 0:
    leap_year = True
  else:
    leap_year = False

print("Leap year(t/f)?", leap_year)

# Sum of a list:
nums = [8, 60, 43, 55, 25, 134, 1]
sum_of_list = 0
for i in nums:
  sum_of_list += i
print("Sum of list is: ", sum_of_list)

# Power:
a = int(input("Insert base of exponensial:"))
b = int(input("Insert power of exponensial:"))
answer = 0
for i in range(b-1):
  answer += a * a
print(a, "to the power of ", b, "=", answer)

# Factorial
n = int(input("Insert a number: "))
answer = 1
for i in range(n,1,-1):
  answer = answer * i

print("n! = ", answer)
