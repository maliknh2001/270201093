#first question
def question1():
  animals = 10
  chicken = 6
  roaster = animals - chicken
  return roaster

#second question
def question2():
  x = 1
  y = 4
  z = 0.25
  eq = (((2*x+y)**2)*(z**0.5))/(x**0.5+y**0.5)
  return eq

#third question
def question3(a,b,c):
  result1 = (-1*b + (((b**2-(4*a*c))))**0.5) / (2*a)
  result2=  (-1*b - (((b**2-(4*a*c))))**0.5) / (2*a)
  x = str(result1)+" "+ str(result2)
  return x

#forth question
def question4():
  i = float(input("Insert temp in celcius: "))
  result = i*1.8 + 32
  return result

#fifth question
def question5():
  side1= float(input("insert side1:"))
  side2= float(input("insert side2:"))
  hypotenious= ((side1**2) + (side2**2))**0.5
  return hypotenious

#6th question (I didn't really understand what question 6 wanted so here is what I understood)
def question6():
  x= 80 
  y= 70 
  distance=490-150
  t_in_h = distance/(x+y)
  t_in_min=t_in_h * 60  
  return t_in_min

#exercise from slides
def exercise():
  easy_pace = 8
  tempo = 6
  original_time= 6*60 + 52 #converted it into minutes
  final_time_min = original_time + (1*easy_pace) + (3*tempo) + (2*easy_pace)
  min_left= int(((final_time_min/60)-(final_time_min//60))*60)
  final_time = str(final_time_min//60) + ":" + str(min_left)
  return final_time

#print statements
print(question1())
print(question2())
print(question3(2,6,-20))
print(question4())
print(question5())
print(question6())
print(exercise())
#in case you see this I already know programming that's why I know how to define a function 

