def is_even(number):
    return number - (number // 10) * 10 == 0 or number - (number // 10) * 10 == 2 or number - (number // 10) * 10 == 4 or number - (number // 10) * 10 == 6 or number - (number // 10) * 10 == 8

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
