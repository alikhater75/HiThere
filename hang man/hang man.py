# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    copyoflettersGuessed=lettersGuessed[:]
    for i in secretWord :
        if i in lettersGuessed :
             del(copyoflettersGuessed[copyoflettersGuessed.index(i)])
        else :
            return False
    return True    




def getGuessedWord(secretWord, lettersGuessed):
    string=''
    for i in secretWord :
        if i in lettersGuessed :
            string+=i
        else :
            string+= '_ '
    return string       



import string
def getAvailableLetters(lettersGuessed):
    available= ''.join(sorted(set(string.ascii_lowercase)-set(lettersGuessed)))
    return available      
    

def hangman(secretWord):
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ',len(secretWord),'letters long')
    print('-----------')
    guessesleft=8
    lettersguessed=[]
    while guessesleft>0:
        print('You have ',guessesleft, 'guesses left.')
        print('Available letters:',getAvailableLetters(lettersguessed))
        guess=input('Please guess a letter: ')
        if guess not in lettersguessed :
            lettersguessed.append(guess)
            if guess in secretWord :
             print('Good guess: ',getGuessedWord(secretWord, lettersguessed))
             print('-----------')
            else :
             print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersguessed))
             print('-----------')
             guessesleft-=1
        else :
            print("Oops! You've already guessed that letter",getGuessedWord(secretWord, lettersguessed))
            print('-----------')
        
        if getGuessedWord(secretWord, lettersguessed)== secretWord :
            return 	'Congratulations, you won!'
    print('Sorry, you ran out of guesses. The word was',secretWord)



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
