# Only greater than 18:
names_list = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]
new_names_list = []
for names in names_list:
  if names[1] >=18:
    new_names_list.append(names[0])

for names in new_names_list:
  print(names)

# Books:
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for book in books:
  value1 = len(book)
  value2 = len(set(book))
  book_dict[book] = (value1, value2)

print(book_dict)

# Update book_dict

for key in book_dict.keys():
  value1 = book_dict[key][0]
  value2 = book_dict[key][1]
  value3= (value1+value2) // 2
  book_dict[key]= value1,value2,value3

print(book_dict)

# Employees:
employees = {}
for _ in range(5):
  name = input("Insert employee name: ")
  salary = float(input("Insert a salary: "))
  employees[name]=salary

print(employees)

# Password checker:
password = input("Insert a password:")
valid = False
if len(password) >=8:
  upper, lower, nums = (0,) * 3
  for char in password:
    if char.isupper():
      upper+=1
    elif char.islower():
      lower+=1
    elif char.isnumeric():
      nums+=1
  if upper > 0 and lower > 0 and nums > 0:
    valid = True

print("Validity:",valid)

# Set 
numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]

set1 = set(numbers1)
set2 = set(numbers2)
intersect = []
for i in set1:
  if i in set2:
    intersect.append(i)

print(intersect)