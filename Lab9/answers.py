"""
Name: Malik
Id: 270201093
Section: 4
Topic: Recursive & iterative functions
This program is used as a medium for answers discussed in lab 9 
"""

#Check that interpreter works:
print("Hello World")

# Q1: harmonics
def harmonic(x):
  if x == 1:
    return 1
  else:
    return harmonic(x-1) + 1/x

print(harmonic(5))