# -*- coding: utf-8 -*-

def single_root_words(root_word: str, *other_words) -> None:
    same_words = []
    root_word_lower = root_word.lower()
    for word in other_words:
        if root_word_lower in word.lower() or word.lower() in root_word_lower:
            same_words.append(word)
    return same_words


if __name__ == "__main__":
    result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
    result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
    print(result1)
    print(result2)
