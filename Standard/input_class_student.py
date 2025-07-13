class student:
    def __init__(self, name, roll_no, department, CGPA):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.CGPA = CGPA

    def is_eligible(self):
        if self.CGPA >= 7:
            return True
        else:
            return False
        
    

num = int(input("How many students are there: "))
students = []

for i in range(num):
    print(f"Enter the details of the student{i+1}:" ) #f is used for formatted string like using the increments like i+1
    name = input("Enter the name of the student: ")
    roll_no = int(input("Enter the roll number: "))
    department = input("Enter the department: ")
    CGPA = float(input("Enter the CGPA: "))

    s = student(name, roll_no, department, CGPA)
    students.append(s) # for adding each student to the students list

def placement(student):
    for x in student:
        if x.is_eligible():
            print(x.name + "Student is eligible for placement")
        else:
            print(x.name + "Not eligible for placement")

placement(students)        