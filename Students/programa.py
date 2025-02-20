# Student Grades System

students = []

while True:
    print("\n=== STUDENT GRADES SYSTEM ===")
    print("1. Register student and grades")
    print("2. Display all students and grades")
    print("3. Calculate average and check approval status")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input("Enter the student's name: ")
        grades = []

        for i in range(3):
            grade = float(input(f"Enter grade {i + 1}: "))
            grades.append(grade)

        students.append([name, grades])
        print("Student successfully registered!\n")

    elif option == "2":
        print("\nList of students and their grades:\n")
        for student in students:
            print(f"Student: {student[0]}\nGrades: {student[1]}\n")

    elif option == "3":
        print("\nAverage Grades and Status:\n")
        for student in students:
            average = sum(student[1]) / len(student[1])
            status = "Approved" if average >= 7 else "Failed"
            print(f"Student: {student[0]}\nAverage: {average:.2f}\nStatus: {status}\n")

    elif option == "4":
        print("Exiting the program...")
        break

    else:
        print("Invalid option! Please choose a valid option.")

        
