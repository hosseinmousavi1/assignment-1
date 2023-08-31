print("check up your health")
a=float(input("enter your weight(in KG):"))
b=float(input("enter your height(in meters): "))
BMI=a/b**2
print("BMI=",BMI)
if BMI<18.5:
    result=("underweight,eat more!")
elif 25>BMI>=18.5:
    result=("normal weight,you have a healthy lifestyle")
elif 30>BMI>=25:
    result=("overweight,eat less!")
elif 35>BMI>=30:
    result=("obesity,exercise more!")
elif 40>BMI>35:
    result=("extreme obesity,you are dying!!")
print(result)