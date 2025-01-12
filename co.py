#grade students based on marks
mark=int(input("enter studen marks"))

if(mark>=90):
    grade="A"
elif(mark>=80 and mark<90):
    grde="B"
elif(mark>=70 and mark<80):
    grade="C"
else:
    grade="D"
print("grade of the student->:",grade)