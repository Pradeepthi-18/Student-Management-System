class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll(self, course):
        if course.course_id not in self.courses:
            self.courses[course.course_id] = course

    def assign_grade(self, course, grade):
        if course.course_id in self.courses:
            self.courses[course.course_id].grades[self.student_id] = grade

    def calculate_gpa(self):
        total_grade_points = 0
        total_credits = 0

        for course_id, course in self.courses.items():
            if self.student_id in course.grades:
                grade = course.grades[self.student_id]
                credit = course.credit
                total_grade_points += grade * credit
                total_credits += credit

        if total_credits == 0:
            return 0
        else:
            return total_grade_points / total_credits


class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit
        self.students = {}
        self.grades = {}

    def enroll_student(self, student):
        if student.student_id not in self.students:
            self.students[student.student_id] = student
            self.grades[student.student_id] = None

class Grade:
    @staticmethod
    def calculate_gpa(grade):
        if grade >= 3.5:
            return 'A'
        elif grade >= 2.5:
            return 'B'
        elif grade >= 1.5:
            return 'C'
        else:
            return 'F'
            
def main():
    students = {}
    courses = {}

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Assign Grade")
        print("5. Calculate GPA")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            students[student_id] = Student(student_id, name)
            print("Student added successfully!")

        elif choice == '2':
            course_id = int(input("Enter course ID: "))
            name = input("Enter course name: ")
            credit = int(input("Enter course credit: "))
            courses[course_id] = Course(course_id, name, credit)
            print("Course added successfully!")

        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            if student_id in students and course_id in courses:
                students[student_id].enroll(courses[course_id])
                courses[course_id].enroll_student(students[student_id])
                print(f"Student {students[student_id].name} is enrolled in {courses[course_id].name} course successfully!")
            else:
                print("Student or course not found!")

        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            grade = float(input("Enter grade: "))
            if student_id in students and course_id in courses:
                students[student_id].assign_grade(courses[course_id], grade)
                print("Grade assigned successfully!")
            else:
                print("Student or course not found!")

        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            if student_id in students:
                gpa = students[student_id].calculate_gpa()
                print(f"Student's GPA: {gpa}")
                grade = Grade.calculate_gpa(gpa)
                print(f"Student's Grade: {grade}")
            else:
                print("Student not found!")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
