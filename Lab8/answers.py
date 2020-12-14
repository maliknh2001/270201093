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
print(summationSquared(a_list))

#Question 2:
def is_prime(number):
  main_list = [2,3,5,7]
  if number in main_list:
    return True
  else:
    for i in main_list:
      if number % i == 0 or number<=1:
        return False
    return True

print(is_prime(1))



