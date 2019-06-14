def recite(start_verse, end_verse):
    f = open("README.md", "r")
    lyrics = [
        line.replace('\n', "") for line in f if line.startswith("On the ")
        ]
    f.close()
    return lyrics[start_verse - 1: end_verse]
