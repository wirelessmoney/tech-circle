# Student Grade Management System in Python
class StudentGradeSystem:
      def __init__(self):
        self.students = {}

def add_student(self, student_name, grades):
    self.students[student_name] = grades 
    print(f"Added student {student_name} with grades {grades}.")

def view_students(self):
    if not self.students:
        print("No students in the system.")     
        return
    
    print("\nStudent Grades:") 
    for student_name, grades in self.students.items(): 
        avg_grade = self.calculate_average(grades) 
        status = "Pass" if avg_grade >= 50 else "Fail" 
        print(f"Name: {student_name}, Grades: {grades}, Average: {avg_grade:.2f}, Status:{status}")

def calculate_average(self, grades):
    return sum(grades) / len(grades)

def update_student(self, student_name, grades):
    if student_name in self.students:
        self.students[student_name] = grades 
        print(f"Updated grades for {student_name}.")
    else:   
        print(f"Student {student_name} not found.")

def delete_student(self, student_name): 
    if student_name in self.students: 
        del self.students[student_name] 
        print(f"Deleted student {student_name}.")
    else:   
        print(f"Student {student_name} not found.")

# Menu to interact with the system def main(): system = StudentGradeSystem()
def main():
      system = StudentGradeSystem

while True:
        print("\n--- Student Grade Management ---")
        print("1. Add Student") 
        print("2. View Students") 
        print("3. Update Student")
        print("4. Delete Student") 
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter student name: ")    
            grades = list(map(float, input("Enter grades separated by space: ").split())) 
            system.add_student(student_name, grades)

        elif choice == '2': system.view_students()

        elif choice == '3':
            student_name = input("Enter student name: ")    
            grades = list(map(float, input("Enter new grades separated by space: ").split()))   
            system.update_student(student_name, grades)

        elif choice == '4':
            student_name = input("Enter student name: ") 
            system.delete_student(student_name)
    
        elif choice == '5':
            print("Exiting...") 
        break

else: 
            print("Invalid choice, please try again.")
        
if __name__ == "__main__":
    main()
