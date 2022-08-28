from tokenize import Double


height= input("Enter your height in m:")
weight= input("Enter your weight in kg:")
print(type(height))
print(type(weight))
BMI=int(weight)/float(height)**2
new_bmi=int(BMI)
print(new_bmi)