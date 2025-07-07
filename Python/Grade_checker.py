# Grade Checker
# Take a score as input and print the grade based on the following:
# 90+ : "A"
# 80-89 : "B"
# 70-79 : "C"
# 60-69 : "D"
# Below 60 : "F"
# here we used a basic if else statement to carry out marks and all.

score = int(input("enter your marks: "))
if score>=90:
    print("Grade A")
elif score<=89 and score>=80:
    print("Grade B")
elif score<=79 and score>=70:
    print("Grade C")
elif score<=69 and score>=60:
    print("Grade D")
else:
    print("Grade F")
