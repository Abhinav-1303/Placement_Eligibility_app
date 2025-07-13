class student:
    def __init__(self, name, roll_no, department, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.cgpa = cgpa

    def is_eligible(self):
        if self.cgpa >= 7:
            return True
        else:
            return False
    
    def update_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa

s1 = student("Mike", 23, "it", 6.3)

#print("Before update cgpa is: " + str(s1.cgpa)) # here we can use either str here or f at the beggining
print(f"Before update cgpa is: {s1.cgpa}")
#print(f"Eligible for placement:  {s1.is_eligible()}")
print("Eligible for placement:", "Yes" if s1.is_eligible() else "No")

new_cgpa = float(input("Enter the new cgpa: "))
s1.update_cgpa(new_cgpa)

print("Eligible for placement: ", "Yes" if s1.is_eligible() else "No")