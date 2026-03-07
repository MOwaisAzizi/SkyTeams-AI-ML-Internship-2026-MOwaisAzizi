
from words import words
import random
import string

def get_valid_word():
    word = random.choice(words)
    # print(word)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

def game():
    word = get_valid_word()
    print(word)
    words_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(words_letter) > 0:
        print('.................')
        print(words_letter)
        print('You already used: ', ' '.join(used_letters))
        currentWordList = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(currentWordList))

        user_letter = input('inter your litter!').upper()
        print(user_letter)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in words_letter:
               print(user_letter)
               words_letter.remove(user_letter)
        elif user_letter in used_letters:
            print('you already used that')
        else:
            print('invaldi chars')
    print('you guessed all🐥🐥'+ word)
game()