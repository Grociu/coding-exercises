def same_vowel_group(words):
    vowels = "aioeu"
    return [
        word
        for word in words
        if set(word) & set(vowels) == set(words[0]) & set(vowels)
    ]
