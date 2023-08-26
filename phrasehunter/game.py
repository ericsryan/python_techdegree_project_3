import random

from .phrase import Phrase

# Create your Game class logic in here.
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def create_phrases(self):
        phrases = [
            Phrase("Hello"),
            Phrase("Howdy"),
            Phrase("Hi"),
            Phrase("Greetings"),
            Phrase("How do you do")
        ]
        return phrases
    
    def get_random_phrase(self):
        return random.choices(self.phrases, k=1)[0]
    
    def get_guess(self):
        user_guess = input("Guess a letter: ")
        return user_guess
    
    def game_over(self):
        if self.missed == 5:
            print("You lost")
        else:
            print("You won")
    
    def start(self):
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            self.welcome()
            print(f"Number missed: {self.missed}\n")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            if not self.active_phrase.check_guesses(user_guess):
                self.missed += 1
            self.guesses.append(user_guess)
        self.game_over()
        
    
    
    def welcome(self):
        print("""
    ============================
      Welcome to Phrase Hunter
    ============================
              """)