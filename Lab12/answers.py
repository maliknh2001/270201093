# Checking code is working
print("hello world")

import math

class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height
  def get_radius(self):
    return self.radius
  def get_height(self):
    return self.height
  def set_radius(self,radius):
    if radius > 0:
      self.radius = radius
  def set_height(self, height):
    if height > 0:
      self.height = height
  def baseArea(self):
    return math.pi * (self.radius ** 2)
  def area(self):
    return 2 * self.baseArea() * self.height
  def volume(self):
    return self.baseArea() * self.height




