# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guesses_so_far = []

    def guess(self, char):
        """A guess of a character is made. Appending class accordingly"""
        if self.status == STATUS_ONGOING:
            if char in self.guesses_so_far:
                self.remaining_guesses -= 1
            elif char not in self.guesses_so_far:
                self.guesses_so_far.append(char)
                if char not in self.word:
                    self.remaining_guesses -= 1
            self.status = self.get_status()
        else:
            raise ValueError("Game is over, no more guesses allowed")
        return 

    def get_masked_word(self):
        """ This returns a masked word for the hangman puzzle. 
        
        If the letter was guessed already, gives the letter, 
        otherwise gives an underscore.
        """
        return "".join(
                char if char in self.guesses_so_far else
                '_' for char in self.word
                )
        

    def get_status(self):
        """ This returns the status of the game. 

        If you won, you won, if you don't have any more guesses you lose.
        """
        if self.get_masked_word() == self.word:
            return STATUS_WIN
        elif self.remaining_guesses < 0:
            return STATUS_LOSE
        else:
            return STATUS_ONGOING