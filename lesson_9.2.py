def difference(*args):
    if len(args) == 0:
        return 0
    max_value = args[0]
    min_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return round(max_value - min_value, 2)
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')