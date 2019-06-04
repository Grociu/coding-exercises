"""
https://www.youtube.com/watch?v=C3Z9lJXI6Qw

Create a sentence object where we expect a string of words, and when we,
loop over this object we simply want to loop through the words in the sentence.
"""

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = sentence.split()
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words): # try/except
            index = self.index
            self.index += 1
            return self.words[index]  
        else:
            raise StopIteration
    
    # I tried using a generator syntaxin this class (yield) and got infinite 
    # loops all around. If I'm trying to do a class solution, it's different
    # than a generator solution. A class definse it's own __iter__ and __next__
    # while a generator explicitely thakes care of that for you


# example generator
def words_from_a_sentence(sentence):
    for word in sentence.split():
        yield word

for word in words_from_a_sentence("This is a test sentence"):
    print(word)
