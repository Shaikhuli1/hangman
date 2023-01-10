# Hangman

This is a game of Hangman I created using basics I learned from Python.

The script can be broken down into three parts:

1. **Constants** - Added a few illustrations in the form of ASCII art to show each step of the hangman. A dictionary of words is there where one will be selected randomly.

2. **Game logic** - A series of functions that carry each aspect of the game.
    1. Randomly selecting a word from the aformentioned dictionary.
		
		```ruby
		def getRandomWord(wordList):
			return random.choice(wordList)
		```
		
    2. Displaying the board state i.e. the hangman, the secret word and guessed letters.
		
		```ruby
		def displayBoard(wrongLetters, rightLetters, secretWord):
			print('\n' + hangmanpics[len(wrongLetters)] + '\n')
			blanks = '_'*len(secretWord)

			print(f'Wrong letters: {wrongLetters}')

			for i in range(len(secretWord)):
				if secretWord[i] in rightLetters:
					blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
			print(blanks)
		```
		
    3. Taking player input and running some validations.
		
		```ruby
		def playerGuess(prevGuesses):
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
		```
			
        1. Checking to see if the input's a single letter.
        2. If the guess is a letter from the English alphabet.
        3. If the guess has already been made on a previous occasion.
        
    4. Asking the player if they wish to play again. 
    
    ```ruby
    def playAgain():
      choice = input('Do you wish to play again? Y or N: ')
    while choice.upper() not in ('Y', 'N'):
        print('Please enter Y or N')
        choice = input('Do you wish to play again? Y or N: ')
    if choice.upper() == 'Y':
        main()
    else:
        print('Thank you for playing')
    ```
3. **Main Script** - Takes the function and consolidates them into a control of sorts.

```ruby
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
```

  * The first part of this initialises the variables as well as a Boolean operator to be able to stop the while loop later.
  * The loop itself displays the state of the board upon each cycle, then using the if statement it decides what it does depending on if the guessed input was correct or not. 
  * Once it does, checks are applied to see if either all the letters have been guessed, or if they've run out of chances.
  * If the player runs out of chances, it'll display the board a final time with the correct answer. Then it'll prompt the player if they wish to go again.
  
    
    
    
    
    
    
    
    
    
    
    
