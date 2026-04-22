from flask import Flask, redirect, url_for, render_template, request

# Create Flask app
app = Flask(__name__)

# HOME ROUTE
@app.route('/')
def home():
    return render_template('home.html')

# BASIC ROUTING EXAMPLES (COMMENTED)
"""
@app.route('/welcome')
@app.route('/wel')
def welcome():
    return 'Hello World\nThis is first flask project'

@app.route('/first')
@app.route('/home')
def home():
    return 'This is homepage debug mode on hello'

app.add_url_rule('/f_url', 'charan', home)
"""

# DYNAMIC ROUTING EXAMPLES (COMMENTED)
"""
@app.route('/profile/<name>')
def profile(name):
    return f"hello guyz i'm {name}"

@app.route('/page_1/<name>/<age>/<desg>')
def page_1(name, age, desg):
    return f'hello {name}\ni was {age}\nI was a {desg}'

@app.route('/<value>')
def new_data(value):
    return f'its a dynamic routing function with value={value}'

@app.route('/wish/<wish>')
def wish(wish):
    return f'Hello this is wish function, wish={wish}'
"""

# REDIRECTION EXAMPLES (COMMENTED)
"""
@app.route('/wish/<name>/<age>')
def wish(name, age):
    return f'hello {name}, your age is {age}'

# Static redirect
@app.route('/call')
def call():
    return redirect(url_for('wish', name='charan'))

# Dynamic redirect
@app.route('/call/<c_name>/<c_age>')
def call(c_name, c_age):
    return redirect(url_for('wish', name=c_name, age=c_age))
"""

# FORM HANDLING - GET METHOD
@app.route('/welcome')
def welcome():
    if request.args.get('new_method') == 'asd':
        name = request.args.get('name')
        location = request.args.get('location')
        return render_template('welcome.html', name=name, location=location)

    return render_template('form.html')

# FORM DISPLAY
@app.route('/show', methods=['GET', 'POST'])
def show():
    return render_template('form1.html')

# FORM HANDLING - POST METHOD
@app.route('/another', methods=['GET', 'POST'])
def another():
    if request.method == 'POST':
        username = request.form.get('user')
        number = request.form.get('number')
        return render_template('welcome.html', name=username, number=number)

    return render_template('form1.html')

# UPDATE (SIMULATING PUT)
@app.route('/update', methods=['GET', 'POST', 'PUT'])
def update():
    if request.method == 'POST':
        if request.form.get('extra_method') == 'PUT':
            updated_number = request.form.get('number')
            return render_template('update.html', number=updated_number)

    return render_template('form2.html')

# DELETE (SIMULATING DELETE)
@app.route('/delete', methods=['GET', 'POST', 'DELETE'])
def delete():
    if request.method == 'POST':
        if request.form.get('extra_method') == 'DELETE':
            deleted_number = request.form.get('number')
            return render_template('delete.html', number=deleted_number)

    return render_template('form3.html')

# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)