class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is " + self.name + " And my age is " + str(self.age))

class student(person):
    def __init__(self,name, age, cgpa, roll_no, department):
        super().__init__(name, age) #way to call parent constructor
        self.cgpa = cgpa
        self.roll_no = roll_no
        self.department = department
    
    def is_eligible(self):
        if self.cgpa >= 7:
            return True
        else:
            return False
        
    def update_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa

s1 = student("Mike", 21, 6.3, 12, "IT")
s1.introduce()

print("Eligible for placement", "Yes" if s1.is_eligible() else "NO")

new_cgpa = float(input(("Enter the new CGPA: ")))
s1.update_cgpa(new_cgpa)

print("Eligible for placement", "Yes" if s1.is_eligible() else "No")


