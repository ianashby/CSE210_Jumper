class Word():
    """Choose a random word, break it into letters, and compare our guesses.

        Attributes:
        _letters []: the word that's being guessed, broken up into a list of letters, guesses
        _guesses []: letters that have been guessed

    """

    def __init__(self):
        """Constructs a new Word
            Args:
                self: an instance of Word
        """
        pass

    def _choose(self):
        """Chooses a random new word out of a list of words
            Returns: the random word
        """
        pass
    
    def guess(self,guess):
        """ Takes a guess, checks if it is in the letters list and adds it to the guesses
            Args:
                guess: a letter from the player
            Returns: 
                a boolean which indicates whether the guess was in the word or not
        """
        pass

    def __str__(self):
        pass