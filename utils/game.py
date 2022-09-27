import random

class Hangman():
    """
    Hangman game class with this methods
    """
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self):
        """
        Initialization of parameters. \n
        :word_to_find: (str) Pick a random words of the list of possible_words. \n
        :lives: (int) Number of possibles errors in the game. \n
        :correctly_guessed_letters: (str) Empty string content for the letters correctly done. \n
        :wrongly_guessed_letters: (str) Empty string content for the letters wrongly done. \n
        :turn_count: (int) \n
        :error_count: (int) \n
        :lettersguessed: (str) \n

        """
        self.word_to_find = (random.choice(Hangman.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ""
        self.wrongly_guessed_letters = ""
        self.turn_count = 1
        self.error_count = 0
        self.lettersguessed = ""


    def start_game(self):
        """"
        Print _ for each letter of the word_to_change and run the play function until lives is on 0
        """

        for letter in self.word_to_find:
            print("_", end=" ")
        print("")

        while self.lives > 0 :
            self.play()
            
        else:
            self.game_over()


    def play(self):
        """
        Ask to user to input a letter and verify if the character is valid or already inputed.
        Verify if the letter is a correct guess or not and add in two diffrents strings contain all the letter inputed by the user correct or not.
        Print _ of eacher missing letter and correct letter in the correct position.
        Decrease the lives if the inputed letter is not in the word to find.
        Print the differents counters of the game.
        And finally verify if the word is founded, run the function well_played or continue to input letter.
        """
        guess = input("Enter a letter : ")

        if len(guess) != 1:
            print("")
            print("Pleaser enter a single letter !")
    
        elif guess in self.lettersguessed:
            print("")
            print("You have already guessed that letter !")

        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("")
            print(f"Sorry but {guess} is not a letter...")

        else:    
            self.lettersguessed = self.lettersguessed + guess

            if guess in self.word_to_find:
                print(f"Correct ! There is \"{guess}\" in the secret word.")
                self.correctly_guessed_letters = self.correctly_guessed_letters + guess

            else:
                self.lives -= 1 
                print(f"Incorrect. There are no \"{guess}\" in the secret word.")
                print("You lost 1 life.")
                self.wrongly_guessed_letters = self.wrongly_guessed_letters + guess

            self.error_count = 0

            print("")
        
            for letter in self.word_to_find:
                if letter in self.lettersguessed:
                    print(f"{letter}", end=" ")
                else:
                    print("_", end=" ")
                    self.error_count += 1

            print("")   
            print("")     
            print(f"Correct letters : {self.correctly_guessed_letters}")
            print(f"Incorrect letters : {self.wrongly_guessed_letters}")
            print(f"Already {self.turn_count} turn(s) and {self.lives} lives left.")
            print("")

            if self.error_count == 0:
                self.well_play()
            
            self.turn_count += 1
              

    def game_over(self):
        """
        Print the game over.
        """
        print("Sorry, you didn't find the secret word, try again !")
        exit()
        

    def well_play(self):
        """
        Print the congrats.
        """
        print(f"Congrats! The secret word was: {self.word_to_find}. You won !")
        exit()


        
