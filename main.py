import random

from hangman_words import wordList

from hangman_art import logo, stages, win, lose

endOfGame = False
chosenWord = random.choice(wordList)
wordLength = range(len(chosenWord))
lives = 6
display = []
guessedLetters = []

for _ in wordLength:
    display += "_"

print(logo)

while not endOfGame:
    alreadyGuessed = ""
    guess = input("Guess a letter: ").lower()
    wrongText = f"Letter {guess} is not in the word. Try again!"

    # Check if letter in chosen word, reveal if yes
    for position in wordLength:
        letter = chosenWord[position]
        if letter == guess:
            display[position] = guess

    # Check if letter has already been guessed before by checking guessed_letters
    if guess not in guessedLetters:
        guessedLetters.append(guess)
        alreadyGuessed = False
    elif guess in guessedLetters:
        print("You've already guessed that letter. \n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        alreadyGuessed = True

    # Reduce lives if wrong and game over conditions
    if guess not in chosenWord and alreadyGuessed == False:
        lives -= 1
        print(wrongText)
        alreadyGuessed = True
    elif guess not in chosenWord and alreadyGuessed == True:
        print(wrongText)

    hangman = stages[lives]
    print(hangman)

    # Game over condition
    if lives <= 0:
        endOfGame = True
        print(lose)
        print(f"The word was {chosenWord}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        endOfGame = True
        print(win)