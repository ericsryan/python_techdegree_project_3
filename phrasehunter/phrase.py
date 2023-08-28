# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        """Display the letters that the player has succesfully guessed"""
        print("\n")
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
        print("\n")

    def check_guesses(self, guess):
        """Check to see if the letter is in the phrase"""
        if guess in self.phrase:
            return True
        return False
    
    def check_complete(self, guesses):
        """Check to see if the player has guessed all the letters"""
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True