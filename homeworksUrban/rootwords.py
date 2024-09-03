def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    result = ", ".join(same_words)
    print(result)
    return same_words

single_root_words("power", "powerful", "banana", "Powerbank", "pig", "Powder", "Powerless")
