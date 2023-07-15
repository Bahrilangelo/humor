# Bro i miss my dad..
# Bro dont sad i have an idea
# What?
# Lets go to the shop and we take milk

import time 

def takeMilk():
    print('Welcome to our shop')
    time.sleep(1)
    print('What do you need?')
    time.sleep(1)
    try:
        take = int(input('Milk for m, Egg for e, Panzer Tank for p, Fat man and little boy for f, Condom for c: '))
        if take == 'm':
            print('D dad is that you?')
            time.sleep(1)
            print('Yes son, i am back')
            time.sleep(1)
            print('Dad i miss you so much')
            time.sleep(1)
            print('I miss you too son')
            time.sleep(1)
            print('Dad where are you all those years?')
            time.sleep(1)
            print('I was in the shop i search the milk')
            time.sleep(1)
            print('**Happy Ending**')
        elif take == 'p':
            print('Ow shot the Germans come here')
        elif take == 'f':
            print('congratulations, world war 3 has begun')
        elif take == 'c':
            print("You won't make the same mistake your father did")
    except TypeError:
        print('Please enter a valid input')
        takeMilk()
    
    