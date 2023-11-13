
from flask import Flask, render_template, request
from tools.simp import add_numbers, sub_numbers
from tools.comp import sum_of_digits, is_palindrome, simp_called
from tools.col import myzip

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result_add = None
    result_sub = None
    result_sum_of_digits = None
    result_is_palindrome = None
    result_myzip = None  

    if request.method == 'POST':
        try:
            operation = request.form['operation']

            if operation == 'add':
                num1 = float(request.form['num1'])
                num2 = float(request.form['num2'])
                result_add = add_numbers(num1, num2)
            elif operation == 'sub':
                num1 = float(request.form['num1'])
                num2 = float(request.form['num2'])
                result_sub = sub_numbers(num1, num2)
            elif operation == 'sum_of_digits':
                num_for_sum = float(request.form['num_for_sum'])
                result_sum_of_digits = sum_of_digits(num_for_sum)
            elif operation == 'is_palindrome':
                num_for_palindrome = float(request.form['num_for_palindrome'])
                result_is_palindrome = is_palindrome(num_for_palindrome)
            elif operation == 'myzip':
                list1 = request.form['list1'].split(',')
                list2 = request.form['list2'].split(',')
                result_myzip = myzip(list1, list2)
            else:
                result_add = "Error: Invalid operation."

        except ValueError:
            result_add = "Error: Please enter valid numbers."

    return render_template('result.html', result_add=result_add, result_sub=result_sub,
                           result_sum_of_digits=result_sum_of_digits, result_is_palindrome=result_is_palindrome,
                           result_myzip=result_myzip)

if __name__ == '__main__':
    app.run(debug=True)
