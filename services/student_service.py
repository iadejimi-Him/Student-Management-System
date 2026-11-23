from models.student import register_student, get_all_students

def register_new_student():
    
    print("\n===== REGISTER NEW STUDENT =====")
    
    
    student_number = input("Enter student number: ").strip()
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    email = input("Enter email (optional): ").strip() or None
    
    
    department_id = input("Enter department ID: ").strip()
    gender = input("Enter gender (Male/Female/Other): ").strip()
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ").strip() or None
    
    
    if not student_number or not first_name or not last_name or not department_id:
        print("student number, first name, last name and department are required")
        return
    
    
    if gender and gender not in ("Male", "Female", "Other"):
        print("Invalid gender. Choose Male, Female, Other.")
        return
    
    
    try:
        department_id = int(department_id)
        
    except ValueError:
        print("Department ID must be a number.")
        return
    
    student_id = register_student(
        student_number,
        first_name,
        last_name,
        email,
        department_id,
        gender or None,
        date_of_birth
    )
    
    
    if student_id is not None:
        print("\nStudent registered successfully!")
        print("Generated Student ID:", student_id)
    else:
        print("\nStudent registration was unsuccessful.")
        
        
def view_all_students():
    
    print("\n===== ALL REGISTERED STUDENTS =====")
    
    students = get_all_students()
    
    if not students:
        print("No student records found.")
        return
    
    print("-" * 100)
    print(f"{'ID':<5} {'STUDENT NUMBER':<20} {'FIRST NAME':<15} {'LAST NAME':<30}")
    print("-" * 100)
    
    
    for student in students:
        print(
            f"{student[0]:<5}"
            f"{student[1]:<20}"
            f"{student[2]:<15}"
            f"{student[3]:<15}"
            f"{str(student[4] or 'N/A'):<30}"
        )
        
    print("-" * 100)
    
    print(f"Total Students: {len(students)}")
        
        
    