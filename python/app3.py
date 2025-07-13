from flask import Flask, render_template, request
import csv

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
        CGPA =float(request.form['CGPA'])
        if not(0<=CGPA<=10):
            error = "CGPA Should be between 0 and 10"
            return render_template('form.html', error = error)
    except ValueError:
        error = "Invalid value"
        return render_template('form.html', error = error)
    
    if CGPA >= 7:
        Eligible = "Eligible for placement"
    else:
        Eligible = "Not Eligible for placement"

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

    with open('student_list.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([Name, Roll_Number, Department, CGPA, Eligible, Grade])

    return render_template('result.html', Name = Name, Roll_Number = Roll_Number, Department = Department, 
                           CGPA = CGPA, Eligible = Eligible, Grade= Grade)

@app.route('/students', methods = ['GET'])
def view_students():
    students = []

    search = request.args.get('search', '').lower()
    selected_filter = request.args.get('filter_status', '')

    try:
        with open('student_list.csv', 'r')as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0].lower()
                roll = row[1].lower()
                eligibility = row[4]

                if search:
                    search_match = (search in name or search in roll)
                else:
                    search_match = True

                if selected_filter:
                    filter_match = (selected_filter == eligibility)
                else:
                    filter_match =True

                if search_match and filter_match:
                    students.append(row)
    except FileNotFoundError:
        error = "File is not found"

        return render_template('students.html', students =[], error = error)
    
    return render_template('students.html', students = students, search = search, selected_filter = selected_filter)

if __name__ == '__main__':
    app.run(debug = True)