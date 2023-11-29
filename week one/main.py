def add_student(database):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    details = input("Enter any other relevant details: ")
    database[name] = {
        'age': age,
        'grade': grade,
        'details': details
    }
    print("Student added successfully!")

def view_student(database):
    name = input("Enter student name: ")
    if name in database:
        student = database[name]
        print("Name:", name)
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        print("Details:", student['details'])
    else:
        print("Student not found in the database.")

def list_all_students(database):
    if len(database) == 0:
        print("No students in the database.")
    else:
        print("List of all students:")
        for name, student in database.items():
            print("Name:", name)
            print("Age:", student['age'])
            print("Grade:", student['grade'])
            print("Details:", student['details'])
            print()

def update_student(database):
    name = input("Enter student name: ")
    if name in database:
        print("Enter new information (leave blank to keep existing value):")
        new_age = input("New Age: ")
        new_grade = input("New Grade: ")
        new_details = input("New Details: ")
        student = database[name]
        if new_age:
            student['age'] = int(new_age)
        if new_grade:
            student['grade'] = new_grade
        if new_details:
            student['details'] = new_details
        print("Student information updated successfully!")
    else:
        print("Student not found in the database.")

def delete_student(database):
    name = input("Enter student name: ")
    if name in database:
        del database[name]
        print("Student deleted successfully!")
    else:
        print("Student not found in the database.")

def main():
    database = {}
    while True:
        print()
        print("Student Database Program")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student(database)
        elif choice == '2':
            view_student(database)
        elif choice == '3':
            list_all_students(database)
        elif choice == '4':
            update_student(database)
        elif choice == '5':
            delete_student(database)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()