from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/course') 
def course():
    return render_template('course.html')
@app.route('/registered', methods=['POST']) 
def registered():
    name = request.form.get('name')
    course = request.form.get('course')
    email = request.form.get('email')
    with open("registered.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((name, course, email)) 
    with open('registered.csv', "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    return render_template('registered.html', students=data)
if __name__ == '__main__':
    app.run(debug=True)