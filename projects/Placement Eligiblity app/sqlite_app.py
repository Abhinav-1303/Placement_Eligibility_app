from flask import Flask, render_template, request, redirect, url_for #redirect to a different url, url_for used to build a url for func name
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/result', methods = ['POST'])
def result():
    Name = request.form['Name']
    Roll_Number = request.form['Roll_Number']
    Department = request.form['Department']

    try:
        CGPA = float(request.form['CGPA'])
        if not (0 <= CGPA <= 10):
            error = "CGPA should be between 0 and 10"
            return render_template('form.html', error = error)
    except ValueError:
        error = "Invalid entry"
        return render_template('form.html', error = error)
    
    Eligible = "Eligible for placement" if CGPA >= 7 else "Not Eligible for placement"

    if CGPA >= 9:
        Grade = "A+"
    elif CGPA >= 8:
        Grade = "A"
    elif CGPA >= 7:
        Grade = "B+"
    elif CGPA >= 6:
        Grade = "B"
    elif CGPA >= 5:
        Grade = "C"
    elif CGPA >= 4:
        Grade = "D"
    else:
        Grade = "F"

    conn = sqlite3.connect('Students.db')
    cur = conn.cursor()

    cur.execute(''' INSERT INTO Students(Name, Roll_Number, Department, CGPA, Eligibility, Grade) VALUES (?, ?, ?, ?, ?, ?)''',
                 (Name, Roll_Number, Department, CGPA, Eligible, Grade))
    
    conn.commit()
    conn.close()

    return render_template('result.html', Name = Name, Roll_Number = Roll_Number, Department = Department, CGPA = CGPA,
                            Eligible = Eligible, Grade = Grade)

@app.route('/students', methods=['GET'])
def view_students():
    search = request.args.get('search', '').lower()
    selected_filter = request.args.get('filter_status', '')

    conn = sqlite3.connect('Students.db')
    cur = conn.cursor()

    query = "SELECT * FROM Students WHERE 1=1"
    params = []

    if search:
        query += " AND (LOWER(Name) LIKE ? OR LOWER(Roll_Number) LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    if selected_filter:
        query += " AND Eligibility = ?"
        params.append(selected_filter)

    query += " ORDER BY CAST(Roll_Number AS INTEGER) ASC"  # ✅ Sort by roll number

    cur.execute(query, params)
    fetched_students = cur.fetchall()  # ✅ store as fetched_students

    conn.close()

    students = []
    for i, student in enumerate(fetched_students, start=1):
        students.append([i] + list(student))  # ✅ Add Sl. No. to beginning

    return render_template('students.html', students=students, search=search, selected_filter=selected_filter)


@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit_students(id):
    conn = sqlite3.connect('Students.db')
    cur = conn.cursor()

    if request.method == 'POST':
        Name = request.form['Name']
        Roll_Number = request.form['Roll_Number']
        Department = request.form['Department']
        try:
            CGPA = float(request.form['CGPA'])
            if not(0 <= CGPA <= 10):
                error = "CGPA Should be between 0 and 10"
                return render_template('form.html', error = error)
            
        except ValueError:
            error = "Invalid entry"
            return render_template('form.html', error = error)
        
        Eligible = "You are eligible for placement" if CGPA >=7 else "You are not eligible for placement"

        if CGPA >= 9:
            Grade = "A+"
        elif CGPA >= 8:
            Grade = "A"
        elif CGPA >= 7:
            Grade = "B+"
        elif CGPA >= 6:
            Grade = "B"
        elif CGPA >= 5:
            Grade = "C"
        elif CGPA >= 4:
            Grade = "D"
        else:
            Grade = "F"

        cur.execute(''' UPDATE Students SET Name = ?, Roll_Number = ?, Department = ?, CGPA = ?, Eligibility = ?,
         Grade = ? WHERE id = ?''', (Name, Roll_Number, Department, CGPA, Eligible, Grade, id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_students'))
    
    cur.execute("SELECT * FROM Students WHERE id = ?", (id,))
    student = cur.fetchone()
    conn.close()
    return render_template('edit.html', student = student)

@app.route('/delete/<int:id>', methods = ['POST'])
def delete_student(id):
    conn = sqlite3.connect('Students.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM Students WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_students'))
    

if __name__ == '__main__':
    app.run(debug = True)


    