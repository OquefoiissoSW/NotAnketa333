from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        gender = request.form.get('gender')
        color = request.form.get('color')

        with open('responses.csv', 'r', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                if (email == row[1]):
                    return render_template("index.html", msg = "This email is already taken")

        with open('responses.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, email, age, str(gender), str(color)])

        return redirect('/thankyou')
    return render_template('index.html', msg="")

@app.route('/thankyou')
def thank_you():
    return "Thanks for your reply!"

if __name__ == '__main__':
    app.run()

