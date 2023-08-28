import os
import random
import string

from .phrase import Phrase


def clear_screen():
    """Clear the screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Create your Game class logic in here.
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.completed_phrases = []
        self.guesses = [" "]
        self.incorrect_guesses = []
        self.last_guess_valid = True

    def reset_game(self):
        """Reinitialize the game"""
        self.missed = 0
        self.guesses = [" "]
        self.incorrect_guesses = []

    def create_phrases(self):
        """Create phrases for the game"""
        phrases = [
            Phrase("Hello"),
            Phrase("Howdy"),
            Phrase("Hi"),
            Phrase("Greetings"),
            Phrase("How do you do")
        ]
        return phrases
    
    def game_over(self):
        """Display game results and allow player to continue"""
        clear_screen()
        if self.missed == 5:
            print("You lost...")
        else:
            self.completed_phrases.append(self.active_phrase)
            print("You won, you were right!")
        print("\nThe phrase was: " + self.active_phrase.phrase + "\n")
        if len(self.completed_phrases) == len(self.phrases):
            print("You guessed all the phrases! Come back later, bye!\n")
        else:
            continue_playing = input("Do you want to play again? Enter 'y' to continue or any other character to quit: ")
            if continue_playing.lower() == 'y':
                self.active_phrase = self.get_random_phrase()
                self.reset_game()
            else:
                print("\nThanks for playing, bye!\n")

    def get_guess(self):
        """Allow the user to submit a guess and make sure it is valid"""
        user_guess = input("Guess a letter: ")
        if not self.valid_guess(user_guess):
            return False
        if user_guess not in self.active_phrase.phrase:
            self.incorrect_guesses.append(user_guess)
        return user_guess.lower()
    
    def get_random_phrase(self):
        """Select a random phrase that hasn't been completed yet"""
        while True:
            new_phrase = random.choices(self.phrases, k=1)[0]
            if new_phrase not in self.completed_phrases:
                return new_phrase
    
    def start(self):
        """Start the game loop"""
        self.active_phrase = self.get_random_phrase()
        while (
            self.missed < 5 and 
            not self.active_phrase.check_complete(self.guesses)
        ):
            clear_screen()
            self.welcome()
            print(f"Number missed: {self.missed}")
            if self.incorrect_guesses:
                print(" ".join(self.incorrect_guesses))
            self.active_phrase.display(self.guesses)
            if not self.last_guess_valid:
                print("Your last guess wasn't valid, try again.")
            user_guess = self.get_guess()
            if not user_guess:
                continue
            if not self.active_phrase.check_guesses(user_guess):
                self.missed += 1
            self.guesses.append(user_guess)
            if self.missed == 5 or self.active_phrase.check_complete(self.guesses):
                self.game_over()

    def valid_guess(self, guess):
        """Confirm that the guess is a valid letter"""
        if (
            len(guess) == 1 and
            guess in string.ascii_letters and
            guess not in self.guesses
        ):
            self.last_guess_valid = True
            return True
        self.last_guess_valid = False
        return False
    
    def welcome(self):
        """Draw the 'welcome' game header"""
        print("""
    ============================
      Welcome to Phrase Hunter
    ============================
              """)