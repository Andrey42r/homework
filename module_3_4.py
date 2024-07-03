def single_root_words(root_words, word=None, *other_words):
    same_words = []
    lower_root_word = root_words.lower()
    for word in other_words:
        if lower_root_word in word.lower() or word.lower() in lower_root_word:
            same_words.append(word)
            return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)