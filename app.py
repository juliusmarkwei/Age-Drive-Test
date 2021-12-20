import time, sys

__ages__ = {'Africa': 18, 'America': 15, 'Caribbean': 18,
            'Asia': 17, 'Europe': 16, 'Oceania': 16}
u_name = input("Please may I know your name: ")
try:
    u_age = int(input('%s, please provide your age here:> ' % u_name))
except ValueError:
    print('You have entered an invalid value')
    exit(0)
time.sleep(1); print('Hey! %s, Welcome to the Drive Age test.' % u_name)
time.sleep(1); u_loc = input("Please where are you from? :> ").capitalize()

data_age = __ages__.values(); data_country = __ages__.keys()
try:
    if u_loc in data_country:
        if u_age in data_age:
            print(); print('Congrats %s, you can drive.' % u_name)
        elif u_age > max(data_age):
            print(); print('Congrats %s, you can drive.' % u_name)
        elif u_age < min(data_age):
            print(); print('Sorry %s, you\'ve not yet reached the age limit.' % u_name)
    else:
        print(); print('Please the location you provided isn\'t accepted.'
                       '\nYou need to follow the format.')
except (NameError, TypeError, Exception):
    print(); print('Sorry, you need to follow the usual format.')
finally:
    print('******     ******     ******     ******     *****')
