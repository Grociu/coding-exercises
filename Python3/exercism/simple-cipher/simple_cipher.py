import random


class Cipher(object):
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = "".join(
                [chr(num)
                 for num
                 in [random.randint(97, 122) for _ in range(100)]]
                )

    def encode(self, text):
        return "".join(
            [chr(num)
             for num
             in [(ord(character) % 97 + ord(coder) % 97) % 26 + 97
                 for character, coder
                 in zip(text, self.key*(len(text) // len(self.key)+1))]]
        )

    def decode(self, text):
        return "".join(
            [chr(num)
             for num
             in [(ord(character) % 97 - ord(coder) % 97) % 26 + 97
                 for character, coder
                 in zip(text, self.key*(len(text) // len(self.key)+1))]]
        )
