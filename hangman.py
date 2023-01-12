import random
import string
hangmanpics = {
    0: '', 
    1: '''
    +---+
        |
        |
        |
       ===''', 
    2: '''
    +---+
    O   |
        |
        |
       ===''', 
    3: '''
    +---+
    O   |
    |   |
        |
       ===''', 
    4: '''
    +---+
    O   |
   /|   |
        |
       ===''', 
    5: '''
    +---+
    O   |
   /|\  |
        |
       ===''', 
    6: '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', 
    7: '''
    +---+
    O   |
   /|\  |
   / \  |
       ==='''}

words = ['cat', 'dog', 'rabbit', 'guinea', 'pig', 'hamster', 'parrot', 'snake',
        'lizard', 'frog', 'chicken', 'cow', 'horse', 'sheep', 'goat', 'duck',
        'turkey', 'deer', 'bear', 'wolf', 'fox', 'moose', 'squirrel', 'mouse',
        'rat', 'elephant', 'giraffe', 'zebra', 'hippo', 'rhino', 'lion', 'tiger',
        'leopard', 'cheetah', 'hyena', 'kangaroo', 'koala', 'panda', 'penguin',
        'seal', 'whale', 'shark', 'dolphin', 'seahorse', 'jellyfish', 'starfish',
        'crab', 'lobster', 'shrimp', 'squid', 'octopus', 'ant', 'beetle', 'butterfly',
        'dragonfly', 'fly', 'grasshopper', 'ladybug', 'mosquito', 'moth', 'spider',
        'wasp', 'bee', 'fish', 'clam', 'crayfish', 'snail', 'turtle', 'frog',
        'toad', 'chameleon', 'alligator', 'crocodile', 'dinosaur', 'snake', 'lizard',
        'monkey', 'ape', 'gorilla', 'chimpanzee', 'orangutan', 'baboon', 'lemur',
        'sloth', 'armadillo', 'badger', 'bear', 'beaver', 'bobcat', 'buffalo',
        'camel', 'cat', 'cattle', 'cheetah', 'chicken', 'chimpanzee',]

class Board:
    def __init__(self):
        self.current_index = 0

    def display_board(self, wrong_letters):
        print('\n' + hangmanpics[len(wrong_letters)] + '\n')

        print(f'Wrong letters: {wrong_letters}')

class GameProgress:
    def __init__(self, correct_word):
        self.correct_word = correct_word
        self.wrong_letters = []
        self.right_letters = []
        self.max_chances = 7
        self.blanks = ['_'] * len(correct_word)
        print(self.blanks)

    def handle_good_guess(self,guess):
        self.right_letters.append(guess) 
    
    def handle_bad_guess(self,guess):            
        self.wrong_letters.append(guess)
        self.max_chances -= 1

    def lose_game(self,hangmanpics):
        if len(self.wrong_letters) == len(hangmanpics)-1:
            print('Out of guesses. You lose!')
            print(f'The secret word was {str(self.correct_word)}')
            return True
        else:
            return False
   
    def check_found_all(self):
        for letter in self.correct_word:
            if letter not in self.right_letters:
                return False                          
        return True

    def display_blanks(self):
        for i in range(len(self.correct_word)):                                                              #Loop replaces underscores with the letter correctly guessed by player
            if self.correct_word[i] in self.right_letters:
                self.blanks = self.blanks[:i] + list(self.correct_word[i]) + self.blanks[i+1:]
        print(self.blanks)
        
class Hangman:
    def __init__(self):
        self.board = Board()
        self.correct_word = list(random.choice(words))
        self.game_progress = GameProgress(self.correct_word)
        self.board.display_board(self.game_progress.wrong_letters)

    def player_input(self):
        while True:
            guess = input('Enter a single letter: ').lower()
            if len(guess) != 1:                                                                               #Validation 
                print('Has to be 1 letter')
            elif guess not in string.ascii_lowercase:                                               
                print('Has to be a letter from the alphabet')
            elif guess in self.game_progress.wrong_letters + self.game_progress.right_letters:
                print('You have already tried this letter')
            else:
                return guess

hangman = Hangman()

while True:
    guess = hangman.player_input()
    if guess in hangman.correct_word:		
        hangman.game_progress.handle_good_guess(guess) 
        hangman.game_progress.check_found_all()
    else:
        hangman.game_progress.handle_bad_guess(guess)
        if hangman.game_progress.lose_game(hangmanpics):
            break

    hangman.game_progress.display_blanks()
    hangman.board.display_board(hangman.game_progress.wrong_letters)	