#first exersize
a=int(input("insert an integer"))
for i in range(1,11):
  print(str(a), "X", i, "=" , a*i)
#exersize 2
b = int(input("how many numbers? "))
even_num=0
for i in range(b):
  c=int(input("Enter an integer: "))
  if c%2 == 0 :
    even_num+=1
result= (even_num /b) * 100
print(str(result)+"%")
