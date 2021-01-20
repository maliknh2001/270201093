# Multiplication table
integer = int(input("Enter an integer: "))
for i in range(1,11):
  multi = i * integer
  print(integer, "X" ,i,"=",multi )

# % of evens
nums = int(input("How many numbers? "))
num_of_evens = 0
for i in range(nums):
  a = int(input("Enter an integer:"))
  if a%2 == 0:
    num_of_evens= num_of_evens + 1
percentage = (num_of_evens / nums) * 100
print(percentage,"%")

# Match digits:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
digit_matched = 0

num1 = num1[::-1]
num2 = num2[::-1]

if len(num1) <= len(num2):
  length = len(num1)
else:
  length = len(num2)

for  i in range(length):
  if num1[i] == num2[i]:
    digit_matched +=1

print(digit_matched)

# Password:
paswrd = "abc123"
user = input("Enter a password: ")
if user == "help":
  print(paswrd[0])
elif user == paswrd:
  print("Welcome!")
else:
  print("Wrong")

# Fibonacci:
fibon = int(input("Insert a number:"))
base = 1
fibon_seq = [1]
for i in range(1,fibon_seq):
  if len(fibon_seq) <2:
    fibon_seq.append(i)
  else:
    ans = fibon_seq[i-1]+fibon_seq[i-2]
    fibon_seq.append(ans)

print(fibon_seq)
