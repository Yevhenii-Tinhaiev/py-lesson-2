def popular_words(text, words):
    text = text.lower()
    text_words = text.split()
    result = {}
    for word in words:
        count = 0
        for t_word in text_words:
            if t_word == word:
                count += 1
        result[word] = count
    return result
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')