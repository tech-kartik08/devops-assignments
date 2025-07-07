# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.

register={}

def menu():
    print("1. Show Grades of Students")
    print("2. Add a new student with its grade")
    print("3. update student info")
    print("4. delete info of student")

while True:
    menu()
    choice=int(input("enter your choice(1-4)"))

    if choice==1:
        print(register)
    elif choice==2:
        name=input("enter student name: ")
        grade=input("enter grade of student: ")
        register[name]=grade
        print(f"{name} is added with {grade} grade")
    elif choice==3:
        name = input("name of student: ")
        if name in register:
            grade=input("enter grade of student: ")
            register[name]=grade
            print(f"{name} is added with {grade} grade")
        else:
            print(f"{name} is not present in register")
    elif choice==4:
        name = input("name of student: ")
        if name in register:
            del register[name]
            print(f"{name} is deleted")
        else:
            print(f"{name} is not present in register")
    else:
        print("inavlid choice. choose between 1-4")




        