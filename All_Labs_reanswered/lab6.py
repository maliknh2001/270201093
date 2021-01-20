# email
email = "ceng113@example.com"
user = input("Insert an email:").lower()
new_email = ""
user = user.split("@")
new_email += user[0].replace(".","") + "@"+ user[1]
if new_email == email:
  print("Logged in")
else:
  print("Incorrect password")

# avergae grade:
student_grades = []
avg_grade = []
ninty_plus = []
num_of_student = int(input("Insert number of students:"))
for i in range(num_of_student):
  mid_term1 = int(input("Insert midterm 1 mark: "))
  mid_term2 = int(input("Insert midterm 2 mark: "))
  final = int(input("Insert final mark: "))
  student_grades.append([mid_term1,mid_term2,final])

for grade in student_grades:
  average = (grade[0] + grade[1])* 0.3 + grade[2] * 0.4
  avg_grade.append(average)

# Above 90 grades:
for avg in avg_grade:
  if avg>=90:
    ninty_plus.append(avg)

# Unique elements:
num_of_items = int(input("Insert number of items:"))
lst = []
for _ in range(num_of_items):
  item = int(input("Insert an item:"))
  if item in lst:
    pass
  else:
    lst.append(item)

print(lst)

# Identity matrix:
matrix = int(input("Insert a number:"))
identity_matrix = []
for i in range(matrix):
  identity_matrix.append([])
  for j in range(matrix):
    identity_matrix[i].append(0)

for i in range(len(identity_matrix)):
  identity_matrix[i][i] = 1

for i in identity_matrix:
  print(i)


