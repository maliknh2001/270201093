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

  def surfaceArea(self):
    return 2 * math.pi * self.radius * self.height

  def area(self):
    return 2 * self.baseArea() + self.surfaceArea()

  def volume(self):
    return self.baseArea() * self.height

anything = Cylinder(3, 5)

print(anything.area())
print(anything.volume())


class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
  
  def get_name(self):
    return self.name
  
  def get_salary(self):
    return self.salary
  
  def set_name(self, name):
    self.name = name
  
  def set_salary(self, salary):
    self.salary = salary
  
  def display_info(self):
    print("Name: ", self.get_name())
    print("Salary: ", self.get_salary())
  

class Company:
  def __init__(self):
    self.employee_list = []

  def get_employee_list(self):
    return self.employee_list
  
  def set_employee_list(self, employee_list):
    self.employee_list = employee_list
  
  def addEmployee(self, new_employee):
    if isinstance(new_employee, Employee):
       self.employee_list.append(new_employee)
  
  def display_all_info(self):
    for employee in self.employee_list:
      employee.display_info()
  
  def average_salary(self):
    total_salary = 0
    for employee in self.employee_list:
      total_salary += employee.salary
    average = total_salary // len(self.employee_list)
    return average




