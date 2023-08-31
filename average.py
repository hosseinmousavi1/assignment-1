print("hello student! calculate your average")
input("first name:")
input("last name:")
a=float(input("the grade of the first lesson:"))
b=float(input("the grade of the second lesson:"))
c=float(input("the grade of the third lesson:"))
av=(a+b+c)/3
print("average=" , av)
if av>=17:
    result=("very well,you are great :D")
elif 17>av>=12:
    result=("good,you are normal")
elif 12>av>=0:
    result=("oh no,you are failed!")
print(result)