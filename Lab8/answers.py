"""
Functions
"""
#checking code is working
print("Hello world")

#Question 1:
a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
def summation(lis):
  sum = 0
  for i in lis:
    sum+=i
  return sum ** 2
print(summation(a_list))