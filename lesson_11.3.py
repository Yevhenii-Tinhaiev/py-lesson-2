def is_even(number):
    last_digit = str(number)[-1]
    return last_digit == '0' or last_digit == '2' or last_digit == '4' or last_digit == '6' or last_digit == '8'

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
