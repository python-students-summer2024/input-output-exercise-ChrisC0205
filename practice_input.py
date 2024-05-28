"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    favorite_vegetable = input("What is your favorite vegetable? ")
    print('Interesting! I also love ' + favorite_vegetable + '!')


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    favorite_number = input ('What is yout favorite number? ')
    print ('Interesting! I also love ' + favorite_number + '!')

def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    name = input('What is your name? ')
    zodiac = input ('How old are you? ')
    print('Interesting! My name is also ' + name + ", and I'm also a " + zodiac + '!')

def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    name = input('What is your name? ')
    age = input ('How old are you? ')
    print('Interesting! My name is also ' + name + ", and I'm also " + age + ' years old!')
