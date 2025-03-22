def is_palindrome(text):
    cleaned_text = ''
    for letter in text:
        if letter.isalpha() or letter.isdigit():
            cleaned_text += letter.lower()
    return cleaned_text == cleaned_text[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")