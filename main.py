# Student Management System
# Demonstrates functions, loops, dictionaries, and user input

students = {}

def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists!")
    else:
        students[name] = []
        print(f"{name} has been added.")

def add_grade():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found!")
    else:
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                students[name].append(grade)
                print(f"Grade {grade} added for {name}.")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. please enter a number.")

def show_report():
    if not students:
        print("No students in the system yet.")
        return
    
    print("\n=== Student Report ===")
    for name, grades in students.items():
        if grades:
            avg = sum(grades) / len(grades)
            print(f"{name}: Grades = {grades}, Average = {avg:.2f}")
        else:
            print(f"{name}: No grades recorded.")
    print("======================\n")

def menu():
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Show Report")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            show_report()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Run the program
main()