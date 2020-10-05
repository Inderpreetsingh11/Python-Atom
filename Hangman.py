import random

words_to_guess = ["apple","banana","movie","song",'test','csharp','python']
guess_list = []
random_word = random.choice(words_to_guess)
chances_left = 10

def generating_guess_list(word = random_word):
    for x in word:
        guess_list.append("_")
    return guess_list


def printing_guess_list(new_list):
    xyz = "".join(new_list)
    return xyz

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def hitandtry(chances_left = chances_left):
    while(chances_left > 0):
        if printing_guess_list(guess_list) == random_word:
            print('\n\nHurray you won!!')
            break
        else:
            guessed_letter = input("Enter the letter you guessed : ")
            if guessed_letter in random_word:
                indexes_to_be_changed = find(random_word, guessed_letter)
                for x in indexes_to_be_changed:
                    guess_list[x] = guessed_letter
                print(printing_guess_list(guess_list))
                print
                print(f"Chances left : {chances_left}")
            else:
                chances_left -= 1
                print(f'Wrong option selected\nChances Left : {chances_left}')
    else:
        print(f"Ohhhooo you loose the game.\nThe correct answer was : {random_word}\nBetter luck next time.")



print("Welcome Developer\nLet's start Hangman\nYou Have 10 chances.")
print
print
generating_guess_list()
print(f"The word to search : {printing_guess_list(guess_list)}")
hitandtry()
