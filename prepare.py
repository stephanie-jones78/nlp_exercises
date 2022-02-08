# imports
import numpy as np
import pandas as pd

import acquire

import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer

from time import strftime

import unicodedata

import json

# *****************************************************************************************************

def basic_clean(string):
    '''
    This function takes in a string as a paramenter and performs the following basic cleaning functions:
        1. lowercase,
        2. normalize unicode, and
        3. remove non-alphanumeric characters
    
    The function returns the cleaned string.
    '''
    # 1. lowercase
    string = string.strip().lower()
    
    # 2. normalize unicode
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    # 3. replace non-alphanumeric characters
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    
    return string

# *****************************************************************************************************

def tokenize(string):
    '''
    This function takes in a string and returns the tokenized version of that string.
    '''
    
    # creating tokenizer object
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    # using tokenizer object on string
    string = tokenizer.tokenize(string, return_str=True)
    
    return string

# *****************************************************************************************************

def stem(string):
    '''
    This function takes in a string, stems each individual word, and then joins
    the stem words back together in the returned string.
    '''
    
    # creating the stem object
    ps = nltk.porter.PorterStemmer()
    
    # creating the stems for each individual word in the string
    stems = [ps.stem(word) for word in string.split()]
    
    # putting the stemmed words back together into string
    string = ' '.join(stems)
    
    return string

# *****************************************************************************************************

def lemmatize(string):
    '''
    This function takes in a string of words, creates a lemmatization object that is applied to 
    each individual word in the string, and then rejoined the split list of lemma string words to
    a single string.
    '''
    
    # create the lemmatization object
    wnl = nltk.stem.WordNetLemmatizer()
    
    # creating a list of string of each word in the article and applying the lemmatize object to each word
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # joining the individual list of lemma string words to a single string of words
    string = ' '.join(lemmas)
    
    return string

# *****************************************************************************************************

def remove_stopwords(string):
    '''
    This function takes in a string of words and splits it into a list of strings for each individual 
    word. It then loops through the list of words and returns a string of the joined string words, 
    excluding the stopwords.
    '''
    
    # splitting the string of words into a list of strings
    words = string.split()
    
    # saving the stop words
    stopword_list = stopwords.words('english')
    
    # looping through the list of words and creating a new list with the words not in the stopwords list
    filtered_words = [word for word in words if word not in stopword_list]
    
    # joining the list of words back to a string of words
    filtered_string = ' '.join(filtered_words)
    
    # # printing number of words removed
    # print(f'Removed {len(string) - len(filtered_string)} stop words.\n> Original string: {len(string)}\n> New string: {len(filtered_string)}')
    # print()
    
    return filtered_string