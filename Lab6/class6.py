#checking code is working
print("hello world")

#question1
email="ceng113@example.com"
inputted_email_raw = input("insert an email:")
inputted_email=""
atcharacter = False
for char in inputted_email_raw:
  if char == "@":
    atcharacter = True
    inputted_email+="@"
  elif char == "." and atcharacter == False:
    inputted_email+=""
  else:
    inputted_email+= char.lower()
   
  
if inputted_email == email:
  print("email is correct")
else:
  print("email is wrong")
  #question 2:
  grades= [[50,90,60],[15,60,75],[99,95,91]]
  average_grade=[]
  summation=0
  for i in grades:
    length=len(i)
    for x in i:
      summation= summation+x
    average=summation/length
    average_grade.append(average)
  print(average_grade)