"""
A little assignment to practice printing text 
output to the Python command line.
Do not run this file... run main.py instead.
"""


def print_with_line_break():
    """
    Prints out the text, 'Hello world!' with a line break at the end
    """
    print('Hello world!\n', end='')


def print_without_line_break():
    """
    Prints out the text, 'Hello world!' without a line break at the end
    """
    print('Hello world!', end='')


def print_with_separator_dash_and_with_line_break():
    """
    Prints out the following words, with dashes "-" between them
    and a line break at the end:
    "Twas", "brillig", "and", "the", "slithy", "toves"
    """
    print('Twas' + '-' + 'brillig' + '-' + 'and' + '-' + 'the' + '-' + 'slithy' + '-' + 'toves\n', end='')


def print_with_separator_dash_and_without_line_break():
    """
    Prints out the following words, with dashes "-" between them
    and without a line break at the end:
    "Twas", "brillig", "and", "the", "slithy", "toves"
    """
    print('Twas' + '-' + 'brillig' + '-' + 'and' + '-' + 'the' + '-' + 'slithy' + '-' + 'toves', end='')