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
        
student1 = student("Mike", 1, "cse", 7.5)
student2 = student("Luke", 2, "cse", 6.5)
student3 = student("Alice", 3, "cse", 8)
student4 = student("Maggie", 4, "mech", 6)

students = [student1, student2, student3, student4]

def placement(student):
    for x in student:
        if x.is_eligible():
            print(x.name + "is eligible for placement")

placement(students)
