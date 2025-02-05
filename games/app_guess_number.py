"""This code is intended to replicate a 'guess the number' game"""

#import needed libraries
from random import *

#define variables
basket = [x if type(x) == type(int()) else None for x in range(0,101)]
shuffle(basket)
sorted_number = choice(basket)
name = input('Please, insert your name: ')

if type(name) == type(str()):
    print(f'Well, {name}, I have got a number between 1-100 and you have to guess it in 8 tries')
    play = input('Do you want to play?')

    if type(play) == type(str()) and (play.lower() == 'si' or play.lower() == 'yes'):
        tries = 8
        start = 0
        while start <= tries and start >=0:
            chosen_number = int(input('Insert a number between 0 and 100: '))
            if type(chosen_number) != type(int()) or (chosen_number < 0 or chosen_number > 100):
                start += 1
                print(f'Non valid number, you have lost an opportunity, you have got {tries - start} tries left')
            elif chosen_number < sorted_number:
                start += 1
                print(f'Your number is inferior than the secret number, you have got {tries - start} tries left')
            elif chosen_number > sorted_number:
                start += 1
                print(f'Your number is superior than the secret number, you have got {tries - start} tries left')
            else:
                start += 1
                print(f'You nailed it! {chosen_number} was the secret number indeed. It has taken {start} tries to guess it')
                break
        if chosen_number == sorted_number:
            print('Final Result: YOU HAVE WON')
        else: print('Final Result: YOU HAVE LOST')
        print('Game is set, hope you enjoyed it!')
                
    else:
        print('You decided not to play, understandable')

else:
    print('Please insert a valid name or surname')
    