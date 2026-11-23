# ===============================

# STUDENT MANAGEMENT SYSTEM

# ===============================

import os

from services.student_service import register_new_student, view_all_students



def display_menu():
    print("\n================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("===================")
    
    
    print("1. Register New Student")
    print("2. View All Students")
    print("3. Search for Student")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Manage Departments")
    print("7. Manage Courses")
    print("8. Manage Enrollments")
    print("9. Generate Student Reports")
    print("0. Exit Application")
    
    print("=======================")
    
def main():
    while True:
        
        os.system("cls") # this clear the terminal output
        
        
        display_menu()
        
        choice = input("Enter your choice: ").strip()
        
        
        
        if choice == "1":
            register_new_student()
            
        elif choice == "2":
            view_all_students()
            
        elif choice == "3":
            print("Search for Student")
            
        elif choice == "4":
            print("Update Student Information")
            
        elif choice == "5":
            print("Delete Student")
            
        elif choice == "6":
            print("Manage Departments")
            
        elif choice == "7":
            print("Manage Courses")
            
        elif choice == "8":
            print("Manage Enrollments")
            
        elif choice == "9":
            print("Generate Student Reports")
            
        elif choice == "0":
            print("Thank you for using the Student Management System")
            
            break
        
        else:
            print("Invalid choice. Please try again.")
            
            
        input("\n press Enter to continue...")
            
            
if __name__ == "__main__":
    main()
            


