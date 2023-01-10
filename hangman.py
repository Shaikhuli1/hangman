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


words = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog",
                "goat", "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose", "mouse", "mule", "newt", "otter", "owl", "panda", "parrot", "pigeon", "python", "rabbit", "ram", "rat", "raven",
                "rhino", "salmon", "seal", "shark", "sheep", "skunk", "sloth", "snake", "spider", "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf", "wombat", "zebra"]


def playAgain():
    choice = input('Do you wish to play again? Y or N: ')
    while choice.upper() not in ('Y', 'N'):
        print('Please enter Y or N')
        choice = input('Do you wish to play again? Y or N: ')
    if choice.upper() == 'Y':
        main()
    else:
        print('Thank you for playing')


def getRandomWord(wordList):
    return random.choice(wordList)


def playerGuess(prevGuesses):
    ''' This function asks for players input and then runs it through some validation '''
    while True:
        guess = input('Enter a single letter: ')
        if len(guess) != 1:
            print('Has to be 1 letter')
        elif guess not in string.ascii_lowercase:
            print('Has to be a letter from the alphabet')
        elif guess in prevGuesses:
            print('You have already tried this letter')
        else:
            return guess


def displayBoard(wrongLetters, rightLetters, secretWord):
    print('\n' + hangmanpics[len(wrongLetters)] + '\n')
    blanks = '_'*len(secretWord)

    print(f'Wrong letters: {wrongLetters}')

    for i in range(len(secretWord)):
        if secretWord[i] in rightLetters:
           blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    print(blanks)

def main():

    print('Welcome to Hangman!')
    wrongLetters = ''
    rightLetters = ''
    secretWord = getRandomWord(words)
    gameDone = False

    while True:
        displayBoard(wrongLetters, rightLetters, secretWord)

        guess = playerGuess(wrongLetters + rightLetters)
        if guess in secretWord:
            rightLetters += guess

            foundAll = True
            for i in range(len(secretWord)):
                if secretWord[i] not in rightLetters:
                    foundAll = False
                    break
            if foundAll:
                print('Well done! You win!')
                gameDone = True
        else:
            wrongLetters += guess

            if len(wrongLetters) == len(hangmanpics)-1:
                displayBoard(wrongLetters, rightLetters, secretWord)
                print('Out of guesses. You lose!')
                print(f'The secret word was {secretWord}')
                gameDone = True
        if gameDone:
            playAgain()


if __name__ == '__main__':
    main()

