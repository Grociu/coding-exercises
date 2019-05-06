import re

def wurst_is_better(txt):
    sentence = txt
    patterns = [
        "Kielbasa", "Chorizo", "Moronga", "Salami", "Sausage", "Andouille",
        "Naem", "Merguez", "Gurka", "Snorkers", "Pepperoni"
        ]
    magic_word = "Wurst"
    for pattern in patterns:
        # checking both uppercase and lowercase
        sentence = re.sub(pattern, magic_word, sentence)
        sentence = re.sub(pattern.lower(), magic_word, sentence)
    return sentence