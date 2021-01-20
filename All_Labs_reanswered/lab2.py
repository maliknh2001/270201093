#  Animals:
animals = 10
chickens = 6
roosters = animals - chickens
print("Roosters: ",roosters)

# Math expression:
x = 1
y = 4
z = 0.25
formula_top = ((2*x+y)**2) * ((z) ** 0.5)
formula_bottom = x ** 0.5 + y ** 0.5
answer = formula_top /formula_bottom
print("Formula answer: ",answer)

# Find the root
a = 2
b = 6
c = -20
discrimanant = (b**2 - (4 * a * c))
root1 = (-b + discrimanant ** 0.5 ) / 2*a
root2 = (-b - discrimanant ** 0.5) / 2*a
print("Roots of equation: ",root1 ,",", root2)

# Temp conversion
t_c = float(input("Insert a temp in C: "))
t_f = t_c * 1.8 + 32
print("Temp in F: ", t_f)

# Hypotenius:
side1 = float(input("Insert side 1: "))
side2 = float(input("Insert side 2: "))
hypotenius = (side1 ** 2 + side2 ** 2)**0.5
print("hypotenius is: ", hypotenius)

# Final question:
carA = 80
carB = 70
distance_between = 490
distance_between_final = 150
distance_travelled = distance_between - distance_between_final
time_between = distance_travelled / (carA + carB)
time_in_min = time_between * 60
print("Time between is: ", time_in_min)
