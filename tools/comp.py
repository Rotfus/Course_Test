
from tools.simp import simp_called

def sum_of_digits(number):
    try:
        digit_sum = sum(int(digit) for digit in str(abs(int(number))))
        return digit_sum
    except ValueError:
        return "Error: Please enter a valid number."

def is_palindrome(number):
    try:
        num_str = str(abs(int(number)))
        return num_str == num_str[::-1]
    except ValueError:
        return False

check_simp_called = simp_called  
