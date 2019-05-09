import re


def does_rhyme(txt1, txt2):
    vowels_txt1 = re.findall('[aieou]', (txt1.lower()).split()[-1])
    vowels_txt2 = re.findall('[aieou]', (txt2.lower()).split()[-1])
    return vowels_txt1 == vowels_txt2