import string

input_str = "a-A"
letters = string.ascii_letters
start_char, end_char = input_str.split('-')
start_index = letters.index(start_char)
end_index = letters.index(end_char)
result = letters[start_index:end_index + 1]
print(result)