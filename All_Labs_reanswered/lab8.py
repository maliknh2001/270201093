import random
# Sum squared
def sum_squre(alist):
  summation = 0
  for i in alist:
    summation += i
  return summation ** 2

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]

print(sum_squre(a_list))
# Prime numbers
def is_prime(num):
  num_string = str(num)
  num_string_length = len(num_string)
  for i in range(2,10**num_string_length):
    if i == num:
      pass
    elif num%i == 0:
      return False
  return True

def print_primes_between(a,b):
  for i in range(a,b):
    if is_prime(i):
      print(i)

# Random list:
def get_rand_list(b,e,N):
  a = []
  for i in range(N):
    c = random.randint(b,e)
    a.append(c)
  return a

def get_overlap(list1,list2):
  intersection = []
  for i in list1:
    if i in list2:
      intersection.append(i)
  intersection = set(intersection)
  return intersection


list1 = get_rand_list(b=0, e=10, N=5)
list2 = get_rand_list(b=0, e=10, N=5)
intersection = get_overlap(list1,list2) 
print(list1, "\n", list2, "\n", intersection)

# binary to decimal and vice versa:
def binary_to_dec(binary):
  length = len(binary)
  answer = 0
  for i in range(length):
    answer += int(binary[i]) * 2 ** (length-1)
    length -= 1
  return answer

def dec_to_binary(decimal):
  text = ""
  while True:
    if decimal == 0:
      break
    else:
      if decimal % 2 == 0:
        text+= "0"
      else:
        text+= "1"
    decimal = decimal // 2
  return text[::-1]


print(binary_to_dec("10010"))
print(dec_to_binary(18))

# Password check
def pass_check(password):
  if len(password)< 8 or not password.isalnum():
    return "Level 0"
  elif password.isnumeric():
    return "Level 1"
  elif password.isalnum():
    return "Level 2"
  else:
    return "Level 3"
