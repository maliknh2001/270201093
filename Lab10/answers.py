# Checking that code is working
print("Hello world")

import time
def count_down(t):
    if t ==0:
        print("Time finished")
        return 0
    else:
        print("time remaining", t)
        time.sleep(1)
        return count_down(t-1)



def recursive_sum(n):
  if n == 1:
    return 1
  else:
    return n + recursive_sum(n-1)

# Exercise 1
def f(n):
  if n == 0:
    return 0
  return f(n-1)+3

print(f(6))

# Exercize 2
def hailstone(x):
  if x == 1:
    return [1]
  else:
    if x%2 == 0:
      return [x] + hailstone(x//2)
    else:
      return [x] + hailstone(3 * x + 1)

def summation(my_list):
  if my_list == []:
    return 0
  else:
    if isinstance(my_list[0],list):
      return summation(my_list[0]) + summation(my_list[:-1])
    else:
      return my_list[0] + summation(my_list[1:])

def pascal_triangle(x):
  if x == 1:
    return [1]
  else:
    return [x-1]+pascal_triangle(x-1)

print(pascal_triangle(3))
