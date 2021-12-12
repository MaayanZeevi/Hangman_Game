#Author:Maayan Zeevi, Date:9/12/2021
#The Game of Hangman
#Exampales: ['a','l','m','c','e','t','r','p','n'] , ['e','l','q','t','r','p','n']
import random

MAX_GUESSES = 6
secret_word =random.choice(open('words.txt').read().split()).strip()
letters_guessed= []
mistakes_made=0

def maxval(some_list):
    max_val = 0
    for val in some_list:
        if val>max_val:
            max_val = val
    return max_val

def word_guessed():
    flag=True
    for i in secret_word:
        if i not in letters_guessed:
            flag=False
    return flag

def print_guessesd():
    str_toPrint=""
    for i in secret_word:
        if i not in letters_guessed:
            str_toPrint=str_toPrint+'_'
        else:
            str_toPrint = str_toPrint +i
    print(str_toPrint)

print("Let's Play HangMan Game:")
while(MAX_GUESSES>0):
    print('Number of left gusses: {}'.format(MAX_GUESSES))
    print_guessesd()
    guess=input("Guess a letter:")
    guess=guess.lower()
    if guess not in letters_guessed:
        letters_guessed.append(guess)
    if(guess not in secret_word): MAX_GUESSES=MAX_GUESSES-1





