from flask import Flask, render_template, redirect, request
import subprocess
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():

    attendance_data = []

    if os.path.exists('attendance.csv'):

        with open('attendance.csv', 'r') as file:

            reader = csv.reader(file)

            next(reader, None)

            for row in reader:

                attendance_data.append(row)

    return render_template(
        'index.html',
        attendance=attendance_data
    )

@app.route('/capture', methods=['POST'])
def capture():

    student_name = request.form['student_name']

    subprocess.Popen(
        ["python", "src/capture.py", student_name]
    )

    return redirect('/')

@app.route('/train')
def train():

    subprocess.Popen(
        ["python", "src/train.py"]
    )

    return redirect('/')

@app.route('/attendance')
def attendance():

    subprocess.Popen(
        ["python", "src/recognize.py"]
    )

    return redirect('/')

if __name__ == '__main__':

    app.run(debug=True)