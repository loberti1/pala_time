"""This code intends to replicate the popular game hangman, basically you have 6 opportunities to try to guess the secret word"""

from random import *
import string
life = 6
palabra = choice(['escuadra','zanata','cheese','outstanding','home','street'])
empty_word = '-' * len(palabra)

def verify(x):
    return '-' in x

def insert_letter():
    """function to choose and get a letter"""
    letter = input('Please, insert a letter: ')
    if letter in list(string.ascii_lowercase):
        return letter
    else: return 'It is not a letter'

def index_letter(word,x):
    """function to obtain indexes for a certain word if the chosen letter is present"""
    indexes = [i for i,j in enumerate(word) if j == x]
    return indexes

def replace_in_blanks(empty_word,x,positions):
    """function to replace '-' with the chosen letter if the letter is indeed present in the word"""
    empty_word = list(empty_word)
    for i in positions:
        empty_word[i] = x
    empty_word = ''.join(empty_word)
    return empty_word

try: 
    while life > 0 and verify(empty_word) == True:
            letra = insert_letter()
            indices = index_letter(palabra,letra)
            empty_word = replace_in_blanks(empty_word,letra,indices)
            print(empty_word)
            life -= 1
            print(f'You have {life} lives left')
            full_word = input('try: ')

            if  full_word == palabra or empty_word == palabra:
                print(f'Congratulations, you have won! Indeed, secret word was {palabra}')
                print('GAME SET')
                break
            else: continue

    if verify(empty_word) == True and life == 0:
        print('Such a pitty, you have lost. But do not hesitate to try again')
        print('GAME SET')
    else: 
        pass
except:
    raise KeyError

    
