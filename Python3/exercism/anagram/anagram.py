def find_anagrams(word, candidates):
    return [
        a for a in candidates if word.lower() != a.lower() and
        sorted(word.lower()) == sorted(a.lower())
        ]
