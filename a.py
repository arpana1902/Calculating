print("Enter Marks Obtained in 6 semester: ")
a = int(input())      # a=first semester
b = int(input())      # b=first semester
c = int(input())      # c=first semester
d = int(input())      # d=first semester
e = int(input())      # e=first semester
f = int(input())      # f=first semester
g = int(input())      # g = Attendance percentage
h = int(input())      # h = extracurricular activities
i = int(input())      # i = Academic awards and achievements
j = int(input())      # j = Coding skills
tot = a+b+c+d+e+f
avg=tot/6             # avg= semester grade

if avg<35 and g<30:
    print("Dropout")
elif avg>60:
    print("good_performance")
elif avg<40:
    print("poor performance")
elif avg>=40 and avg<60:
    print("support required")
elif avg>65 and j or i or h:
    print(" eligibility for placement ")
else:
    print("Invalid Input!")