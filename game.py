import random

class Hangman():
    """Hangman game class with this methods"""

    possible_words = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self):
        """Initialization of game parameters."""
        self.word_to_find = (random.choice(Hangman.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ""
        self.wrongly_guessed_letters = ""
        self.turn_count = 1
        self.error_count = 0
        self.lettersguessed = ""
        self.guess = ""

    def start_game(self):
        """Conditions to lose or win"""
        for letter in self.word_to_find:
            print("_", end=" ")
        print("")

        while self.lives > 0:
            self.play()
            if self.error_count == 0:
                self.well_play()    
        else:
            self.game_over()

    def play(self):
        """Run the game"""
        self.guess = input("Enter a letter : ")
        
        if len(self.guess) != 1:
            print("")
            print("Pleaser enter a single letter !")
        elif self.guess in self.lettersguessed:
            print("")
            print("You have already guessed that letter !")
        elif self.guess not in "abcdefghijklmnopqrstuvwxyz":
            print("")
            print(f"Sorry but {self.guess} is not a letter...")

        else:    
            self.check_letter_in_word_find()
            self.display_word_to_find()
            self.display()
            self.turn_count += 1
              
    def game_over(self):
        """Print the game over."""
        print("Sorry, you didn't find the secret word, try again !")
        exit()
        
    def well_play(self):
        """Print the congrats."""
        print(f"Congrats! The secret word was: {self.word_to_find}. You won !")
        exit()

    def display(self):
        """Print some informations during the game."""
        print("")   
        print("")     
        print(f"Correct letters : {self.correctly_guessed_letters}")
        print(f"Incorrect letters : {self.wrongly_guessed_letters}")
        print(f"Already {self.turn_count} turn(s) and {self.lives} lives left.")
        print("")

    def check_letter_in_word_find(self):
        """Conditions to guess right or false letter"""
        self.lettersguessed += self.guess
        if self.guess in self.word_to_find:
            print(f"Correct ! There is \"{self.guess}\" in the secret word.")
            self.correctly_guessed_letters += self.guess
        else:
            self.lives -= 1 
            print(f"Incorrect. There are no \"{self.guess}\" in the secret word.")
            print("You lost 1 life.")
            self.wrongly_guessed_letters += self.guess

    def display_word_to_find(self):
        """Print word to find with blind letters"""    
        print("")
        self.error_count = 0
        for letter in self.word_to_find:
            if letter in self.lettersguessed:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
                self.error_count += 1