def second_index(text, some_str):
    index = -1
    for _ in range(2):
        index = text.find(some_str, index + 1)
        if index == -1:
            return None
    return index
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
