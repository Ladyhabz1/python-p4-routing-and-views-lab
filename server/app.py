#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Route for index page
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Print to console
    return text  # Display in browser

# Route to count numbers up to given integer
@app.route('/count/<int:number>')
def count(number):
    return "<br>".join(str(i) for i in range(number))

# Route to perform mathematical operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return "Invalid operation", 400  # Return error for invalid operations

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
