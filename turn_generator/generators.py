import os
import time
from random import *
from datetime import datetime,date

class Customer:
    """class that defines a customer indicating time of the day in wich he/she enters the drugstore and generates a turn"""
    def __init__(self,day,month,year,weekday,hour):
        self.day = day
        self.month = month
        self.year = year
        self.weekday = weekday
        self.hour = hour
    
    def turn_generator(self,area):
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
    """process that generates a number depending on the selection"""
    to_day = Customer(datetime.now().day,datetime.now().month,datetime.now().year,datetime.now().weekday(),datetime.now().hour)
    pharmacy = to_day.turn_generator('pharmacy')
    perfumerie = to_day.turn_generator('perfumerie')
    cosmetics = to_day.turn_generator('cosmetics')
    try:
        while (to_day.hour >= 9 and to_day.hour <= 20 or to_day.weekday != 6):
            print(f'{to_day.year}-{to_day.month}-{to_day.day}')
            print('######################################\nWelcome, please take your turn in your selected area\n######################################')
            print('PHARMACY\nPERFUMERIE\nCOSMETICS')
            selection = str(input()).lower()
            if selection not in {'pharmacy','perfumerie','cosmetics'}:
                os.system('cls')
                print('Your selection is not valid, please try again')
                time.sleep(2.5) 
                os.system('cls')
            elif selection == 'pharmacy':
                os.system('cls')
                print('########################################')
                print (f'Thank you for your time, your turn is:\n{next(pharmacy)}\nYou will be taken care of soon')
                print('########################################')
                time.sleep(2.5)
                os.system('cls')
            elif selection == 'perfumerie':
                os.system('cls')
                print('########################################')
                print (f'Thank you for your time, your turn is:\n{next(perfumerie)}\nYou will be taken care of soon')
                print('########################################')
                time.sleep(2.5) 
                os.system('cls')
            elif selection == 'cosmetics':
                os.system('cls')
                print('########################################')
                print(f'Thank you for your time, your turn is:\n{next(cosmetics)}\nYou will be taken care of soon') 
                print('########################################')
                time.sleep(2.5)
                os.system('cls')
            else:
                print('a critial error has ocurred')
                time.sleep(2.5)
    except:
        print('CRITICAL FAILURE, POWER OFF')
        raise ConnectionAbortedError
    finally:
        print('Power Off')