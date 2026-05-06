from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form['name']
    age=request.form['age']
    email=request.form['email']
    course=request.form['course']
    return render_template('result.html', name=name, age=age, email=email, course=course)

if __name__=='__main__':
    app.run(debug=True)