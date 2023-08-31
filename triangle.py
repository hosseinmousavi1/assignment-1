print("triangle test")
a=float(input("enter the size of the first side:"))
b=float(input("enter the size of the second side:"))
c=float(input("enter the size of the third side:"))
if (a+b>c and b+c>a and a+c>b):
    result=("yes!it is possible")
else:
    result=("no,it is not possible")
print(result)