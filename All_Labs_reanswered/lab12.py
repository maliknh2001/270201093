import math
class Cylinder:
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height
  
  def get_radius(self):
    return self.radius
  
  def get_height(self):
    return self.height
  
  def set_radius(self, radius):
    self.radius = radius
  
  def set_height(self,height):
    self.height = height
  
  def base_area(self):
    return math.pi * (self.radius) ** 2
  
  def surface_area(self):
    return 2 * math.pi * self.height * self.radius
  
  def area(self):
    return 2 * self.base_area() + self.surface_area()
  
  def volume(self):
    return self.base_area() * self.height
  

a = Cylinder(3,5)
print(a.area())
print(a.volume())

class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  
  def get_name(self):
    return self.name
  
  def get_salary(self):
    return self.salary
  
  def set_name(self,name):
    self.name = name
  
  def set_salary(self, salary):
    self.salary = salary
  
  def employee_info(self):
    print("Employee Name:",self.name)
    print("Employee Salary:",self.salary)
  

class Company:
  def __init__(self):
    self.employee_list = []
  
  def get_employee_list(self):
    return self.employee_list
  
  def set_employee_list(self, employee_list):
    self.employee_list = employee_list
  
  def add_employee(self, new_employee):
    if isinstance(new_employee, Employee):
      self.employee_list.append(new_employee)
  
  def average_salary(self):
    num_of_employees = len(self.employee_list)
    sum_salary = 0
    for employee in self.employee_list:
      sum_salary += employee.get_salary()
    average = sum_salary / num_of_employees
    return average
  
  def display(self):
    for employee in self.employee_list:
      employee.employee_info()


class DNA:
  def __init__(self, dna_string):
    self.dna_string = dna_string
  
  def count_nucleotides(self):
    dna_dict = {"A":0,"C":0,"G":0,"T":0}
    if "A" in self.dna_string:
      dna_dict["A"] = self.dna_string.count("A")
    if "C" in self.dna_string:
      dna_dict["C"] = self.dna_string.count("C")
    if "G" in self.dna_string:
      dna_dict["G"] = self.dna_string.count("G")
    if "T" in self.dna_string:
      dna_dict["T"] = self.dna_string.count("T")
    return dna_dict



  