"""
Name: Malik
Id: 270201093
Section: 4
Topic: Recursive & iterative functions
This program is used as a medium for answers discussed in lab 9 
"""
import time

# Checking that interpreter works:
print("Hello World")

# Q1: harmonics
def harmonic(x):
  if x == 1:
    return 1
  else:
    return harmonic(x-1) + 1/x

print(harmonic(5))

# Q2: reverse function
def get_reversed(lis):
  if len(lis) == 0:
    return []
  else:
    return [lis[-1]]+ get_reversed(lis[:-1])

print(get_reversed([1,2,3,4]))

# Q4: number of evens
def get_evens(lis):
  if len(lis)==0:
    return 0
  else:
    if lis[-1]%2 == 0:
      return 1+get_evens(lis[:-1])
    else:
      return get_evens(lis[:-1])

print(get_evens([0,1,2,3]))

# Q5: Countdown
def count_down(t):
  if t == 0:
    return 0
