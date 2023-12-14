import random

def hangman():
    words = ['Javascript', 'Python', 'Java', 'Kotlin', 'Ruby']
    word = random.choice(words).lower()  # Convert the word to lowercase
    guessed_letters = []
    tries = 6

    print('Welcome to Hangman! The topic is programming languages and the word is', len(word), 'letters long. You have', tries, 'tries.')

    while tries > 0:
        guessed_word = ''
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += '_'

        print(guessed_word)

        if guessed_word == word:
            print('Congratulations! You guessed the word correctly.')
            break

        guess = input('Enter a letter or guess the word: ').lower()

        if guess == word:
            print('Congratulations! You guessed the word correctly.')
            break
        
        elif guess in guessed_letters:
            print('You already guessed that letter. Try again.')
        elif guess in word:
            guessed_letters.append(guess)
            print('Good guess!')
        else:
            tries -= 1
            print('Wrong guess. You have', tries, 'tries left.')

    if tries == 0:
        print('Game over. The word was', word)

hangman()
