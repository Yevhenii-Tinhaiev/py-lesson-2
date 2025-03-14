import string
input_string = input("Enter the line: ")
cleaned_word = "".join([symbol for symbol in input_string if symbol not in string.punctuation])
words = cleaned_word.split()
hashtag = "".join([word.capitalize() for word in words])
if len(hashtag) > 140:
    hashtag = hashtag[:140]

hashtag = "#" + hashtag
print(hashtag)