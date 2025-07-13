import csv
import random

names = ["Arun", "Neha", "Ravi", "Divya", "Kiran", "Meera", "Rahul", "Sneha", "Amit", "Pooja",
         "Rakesh", "Nithya", "Sanjay", "Latha", "Vivek", "Anjali", "Rohit", "Deepti", "Manoj", "Swathi",
         "Gaurav", "Harsha", "Anita", "Kavya", "Pranav", "Ishita", "Yash", "Shreya", "Naveen", "Ankita"]

departments = ["CSE", "IT", "Civil", "EEE", "ECE", "Mechanical", "Cyber Security"]

def generate_grade(cgpa):
    if cgpa >= 9:
        return "A+"
    elif cgpa >= 8:
        return "A"
    elif cgpa >= 7:
        return "B+"
    elif cgpa >= 6:
        return "B"
    elif cgpa >= 5:
        return "C"
    elif cgpa >= 4:
        return "D"
    else:
        return "F"

with open('student_list.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for i in range(30):
        name = random.choice(names)
        roll_number = 100 + i
        department = random.choice(departments)
        cgpa = round(random.uniform(3.0, 10.0), 2)
        eligible = "Eligible for placement" if cgpa >= 7 else "Not Eligible for placement"
        grade = generate_grade(cgpa)
        writer.writerow([name, roll_number, department, cgpa, eligible, grade])

print("✅ 30 students added to student_list.csv")
