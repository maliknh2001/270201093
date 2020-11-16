#first exersize
a=int(input("insert an integer"))
for i in range(1,11):
  print(str(a), "X", i, "=" , a*i)
#exersize 2
b = int(input("how many numbers? "))
even_num=0
for i in range(b):
  c=int(input("Enter an integer: "))
  if c%2 == 0 :
    even_num+=1
result= (even_num /b) * 100
print(str(result)+"%")

#excersize3
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
match = 0
if len(num1) > len(num2):
  for i in reversed(num1):
    for x in reversed(num2):
      if x == i:
        match+=1
else:
  for i in reversed(num2):
    for x in reversed(num1):
      if x == i:
        match+=1

print(match)

#excersize 4
pin= "abc123"
x=""
while x != pin:
  x=input("Enter a password")
  if x == "help":
    print(pin[0])
  elif x == pin:
    print("Welcome")
    break
  else:
    print("Wrong")