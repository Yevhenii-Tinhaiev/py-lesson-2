import string
import keyword

test_data = ["_", "__", "___", "x", "get_value", "get value", "get!value",
             "some_super_puper_value", "Get_value", "get_Value", "getValue",
             "3m", "m3", "assert", "assert_exception"]

for test_variable_name in test_data:
    if test_variable_name in keyword.kwlist:
        print(f"{test_variable_name} => False")
        continue

    if test_variable_name[0].isdigit():
        print(f"{test_variable_name} => False")
        continue

    up = False
    for symbol in test_variable_name:
        if symbol.isupper():
            up = True
            break
    if up:
        print(f"{test_variable_name} => False")
        continue

    for symbol in test_variable_name:
        if symbol in string.punctuation and symbol != "_":
            print(f"{test_variable_name} => False")
            break
        if symbol == " ":
            print(f"{test_variable_name} => False")
            break
    else:
        underscore = 0
        i = 0
        while True:
            i = test_variable_name.find('_', i)
            if i == -1:
                break
            underscore += 1
            i += 1

        if underscore > 1:
            print(f"{test_variable_name} => False")
        else:
            print(f"{test_variable_name} => True")
