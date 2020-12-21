"""
Functions
"""
#checking code is working
print("Hello world")

#Question 1:
a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
def summationSquared(num_lis):
  sum = 0
  for i in num_lis:
    sum+=i
  return sum ** 2


#Question 2: (will work for only prime numbers between 1 and 121)
def is_prime(number):
  main_list = [2,3,5,7]
  if number in main_list:
    return True
  else:
    for i in main_list:
      if number % i == 0 or number<=1:
        return False
    return True



def print_primes_between(a,b):
  for i in range(a,b+1):
    if is_prime(i):
      print(i)



# Question 4
def binary_to_dec(num):
  a = 0
  for i in range(len(num)):
    res = int(num[i]) * (2**(len(num)-i-1))
    a+=res
  return a

def dec_to_binary(num):
  x = num
  result = []
  while x !=0:
    res = x%2
    result.append(str(res))
    x = x//2
  result= result[::-1]
  final = "".join(result)
  return final

# Question 5
def pass_check(pss):
  Level = 0
  if len(pss)<8 or pss.find(" ") != -1:
    return Level
  elif pss.isnumeric() or pss.isalpha:
    Level+=1
    return Level
  elif pss.isalnum():
    Level+=2
    return Level
  else:
    Level+=3
    return Level


