import os
from random import *
import unittest as uni
from datetime import datetime,date

class Customer:
    def __init__(self,day,month,year,weekday):
        self.day = day
        self.month = month
        self.year = year
        self.weekday = weekday
to_day = Customer(datetime.now().day,datetime.now().month,datetime.now().year,datetime.now().weekday())

def turn_generator(area):
    PH = 1
    PE = 1
    CS = 1
    while type(area) == type(str()):
        if area == 'pharmacy':
            yield 'PH-'+str(PH)
            PH  = PH+1
        elif area == 'perfumerie':
            yield 'PE-'+str(PE)
            PE += 1
        elif area == 'cosmetics':
            yield 'CS-'+str(CS)
            CS += 1
        else: pass

def program_start():
    pharmacy = turn_generator('pharmacy')
    perfumerie = turn_generator('perfumerie')
    cosmetics = turn_generator('cosmetics')
    try:
        while (datetime.now().hour >= 9 and datetime.now().hour <= 20 or to_day.weekday != 6):
            print(f'Today is {to_day.year}-{to_day.month}-{to_day.day}')
            print('#####################################################')
            print('Welcome, please take your turn in your selected area:')
            print('PHARMACY\nPERFUMERIE\nCOSMETICS')
            selection = str(input()).lower()
            if selection not in {'pharmacy','perfumerie','cosmetics'}:
                os.system('cls')
                print('Your selection is not valid, please try again') 
            elif selection == 'pharmacy':
                os.system('cls')
                print (f'Thank you for your time, your turn is: {next(pharmacy)}, you will be taken care of soon')
            elif selection == 'perfumerie':
                os.system('cls')
                print (f'Thank you for your time, your turn is: {next(perfumerie)}, you will be taken care of soon')
            elif selection == 'cosmetics':
                os.system('cls')
                print(f'Thank you for your time, your turn is: {next(cosmetics)}, you will be taken care of soon') 
            else:
                print('a critial error has ocurred')
    except:
        print('CRITICAL FAILURE, POWER OFF')
        raise ConnectionAbortedError
    finally:
        print('Power Off')