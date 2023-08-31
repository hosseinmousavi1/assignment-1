import math
print("superior intelligence is at your service,please select the desired operation:")
print("+:sum , -:sub , *:mul , /:div , !:fact , √:sqrt , sin , cos , tan , cot")
op=input()
if op==("+"or"-"or"*"or"/"):
    x=float(input("enter the first number:"))
    y=float(input("enter the second number:"))
elif op==("!"or"√"):
    x=float(input("enter the number:"))
else:
    x=float(input("enter the angle(by degree):"))
if op=="+":
    result=x+y
elif op=="-":
    result=x-y
elif op=="*":
    result=x*y
elif op=="/":
    if y==0:
        result="incalculable"
    else :
        result=x/y
elif op=="!":
    result:math.factorial(x)
elif op=="√":
    if x>=0:
        result=math.sqrt(x)
    else:
        result=("incalculable")
elif op=="sin":
    result=math.sin(x*math.pi/180)
elif op=="cos":
    result=math.cos(math.radians(x))
elif op=="tan":
    result=math.tan(x*math.pi/180)
elif op=="cot":
    result=1/math.tan(math.radians(x))
print(result)