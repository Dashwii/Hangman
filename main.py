import random
from word_list import WORDS
HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def game():
    playing = True
    while playing:
        win = False
        guessed_letters = set()
        guesses_left = 7
        chosen_word = random.choice(WORDS)

        while guesses_left > 1:
            print(HANGMAN_PICS[-guesses_left])
            [print("_", end="") if letter not in guessed_letters else print(letter, end="") for letter in chosen_word]
            letter = input("\n>")
            if letter in guessed_letters:
                print("You've already guessed this letter!")
                continue
            if letter not in chosen_word:
                if len(letter) > 1:
                    print("Only one letter at a time!")
                    continue
                guesses_left -= 1
            guessed_letters.add(letter)
            if set(chosen_word).issubset(guessed_letters):
                win = True
                break
        if win:
            print("You won!")
        else:
            print("You lose!")
        print(f"Chosen word was {chosen_word}!")
        choice = input("Play again? Y/N:")
        if choice.lower() not in ["y", "yes"]:
            playing = False


game()
