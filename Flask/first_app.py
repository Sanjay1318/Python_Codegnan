from flask import Flask, redirect

a = Flask(__name__)  # flask object

@a.route('/', methods=['GET'])
@a.route('/welcome')
@a.route('/wel')
def welcome():
    return 'Hello World\nThis is first flask project'

@a.route('/first') 
@a.route('/home') # static routing
def home():
    return 'This is homepage debug mode on hello'

@a.route('/profile/<name>') # dynamic routing
def profile(name):
    return f"Hello {name}"

@a.route('/page_1/<name>/<age>/<desgnation>')
def page_1(name,age,designation):
    data =  f"Hello I am {name} and I am {age} years old .\n I am a {designation}"
    return data

# @a.route('/<value>') # without any type cast
@a.route('/<int:value>') # type casting (now it takes only int type)
def new_data(value):
    return f"It's a Dynamic Routing function, with a value in parameter {value}"

@a.route('/<path:value>') # opening the file using path and should always use / slash instead of \
def new_data(value):
    with open(value,"r") as file:
        x = file.read()
    return x

                        # redirecting a function -- abstraction
@a.route('/test')
def test():
    return redirect(valued_function) # can redirect to any function just by keeping the function name in the redirect() paranthesis, 
                                     # also only single argument is allowed

@a.route('/valued')
def valued_function():
    return f"Hello this is a valued function"



if __name__ == '__main__':
    a.run(debug=True,port=5001) # to run the server