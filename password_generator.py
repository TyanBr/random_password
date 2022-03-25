from random import random
import nltk
from nltk.corpus import wordnet
import random

#you will need to download this data set if you do not already have it loaded as it does not come preinstalled with NLTK
#nltk.download('omw-1.4')

def password_generator():
    password = ''
    special_Characters  = '!"£$%^&*()[]:;@#~?<>'
    divider = lambda x: random.choice(x)
    doubler = lambda x: x + x
    password = doubler(divider(special_Characters))
    city = input('What is a city you like that you have visited?')
    password = password + city + doubler(divider(special_Characters))
    word1 = input('What is a word that you like (do not type a name) ')
    def synonym(x):
        synonym_list =[]
        for syn in wordnet.synsets(x): 
            for lemm in syn.lemmas(): 
                synonym_list.append(lemm.name())
        return random.choice(synonym_list)
    password = password + synonym(word1) + doubler(divider(special_Characters))
    word2 = input('What is a second word that you like (do not type a name) ')
    password = password + synonym(word2) + str(random.randint(0,99))
    return print(password)

password_generator()