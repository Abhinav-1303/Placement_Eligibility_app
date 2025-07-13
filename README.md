# Placement Eligibility App 🎓

A Flask-based web application to manage and evaluate student placement eligibility based on CGPA.

## 🚀 Features

- Add student records with CGPA, department, and roll number
- Automatically calculate:
  - **Eligibility** (`Eligible for placement` if CGPA ≥ 7)
  - **Grade** (`A+`, `A`, `B+`, etc.)
- View all students in a searchable, filterable Bootstrap-styled table
- Edit or delete existing students
- Data stored using **SQLite3**
- Sl. No. and **sorted view by Roll Number**
- Responsive UI with Bootstrap 5

# To Run This

git clone https://github.com/Abhinav-1303/Placement_Eligibility_app.git
cd Placement_Eligibility_app
pip install flask
python sqlite_app.py
