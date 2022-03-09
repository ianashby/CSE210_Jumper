from game.jumper import Jumper
from game.terminal import Terminal
from game.word import Word

class Director:
    """Composes everything together."""

    def __init__(self):
        self.jumper = Jumper()
        self.terminal = Terminal()
        self.word = Word()

    def __str__(self) -> str:
        results = ""
        results += self.word._word
        results += "\nYou have guessd: "
        results += str(self.word._guesses)

    def run(self):
        """Starts the game loop"""
        print('Welcome to Jumper')
        
        while not self.jumper.is_dead:
            self.do_updates()
            self.do_outputs()
        self.do_outputs()

    def do_updates(self):
        """Check for changes"""
        guess =self.terminal.guess_letter()
        is_in_word =self.word.guess(guess)
        if(not is_in_word):
            self.jumper.break_chute()

    def do_outputs(self):
        """Prints out new game screen"""
        self.terminal.write_outputs(self.jumper,self.word)
        
    