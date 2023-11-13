
simp_called = False

def add_numbers(num1, num2):
    try:
        result = num1 + num2
        return result
    except ValueError:
        return "Error: Please enter valid numbers."

def sub_numbers(num1, num2):
    try:
        result = num1 - num2
        return result
    except ValueError:
        return "Error: Please enter valid numbers."
