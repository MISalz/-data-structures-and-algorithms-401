from data_structures. hashtable import Hashtable
import re

def first_repeated_word(word):
    '''
    CC31
    Write a function called repeated word that finds the first word to occur more than once in a string

    Arguments: string
    Return: string
    '''
    # split words by spaces
    regex = re.compile('[^a-zA-Z ]')
    stripped_words = regex.sub('', word)
    words = stripped_words.lower().split()
    dictionary = set()

    for word in words:
        if word in dictionary:
            return word
        else:
            dictionary.add(word)
