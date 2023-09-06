#
# CSCI 121 Fall 2021
#
# Project 2, Part 2
#
# chats.py
#
# Process a text and distill statistics about the bi-gram and tri-gram
# word occurrences in the entered text. It does this by using a dictionary
# of words and bi-grams. Each dictionary entry gives the list of words
# in the text that follow that word/bi-gram (and possibly a count of the
# number of times each follower does so).
#
# The code then generates random text based on these statistics.
#
#
# Usage: python3 chats.py
#
# This command processes a series of lines of text, looking for
# contiguous runs of alphabetic characters treating them each as a
# word. For each such word, it keeps a count of the number of its
# occurrences in the text.
#
# To end text entry hit RETURN and then CTRL-d.  It then generates
# a random text that tries to mimic the text it just processed.
#
#
# Alternative usage: python3 chats.py < textfile.txt
#
# The above instead processes the text of the file in 'textfile.txt'.
#

import sys
import random

STOPPERS   = [".", "!", "?"]
WHITESPACE = [" ","\n","\r","\t"]

def simplifyWord(word):
    """Returns the given string with only certain chars and lowercase.

    This "simplifies" a word so that it only contains a sequence of
    lower case letters and apostrophes, making uppercase letters
    lowercase, and skipping others.  It returns the "simplified" word.
    If, upon simplifying a word, all the characters are skipped, the
    function returns None.

    In normal use, this would convert a word like "Ain't" into the
    word "ain't" and return it. It also would take a text string like
    "it105%s" and give back the string "its".

    This particular function behavior is somewhat arbitrary, written
    to be "good enough" just to handle the spurious other characters
    that might arise in the kinds of free texts from things like
    Project Gutenberg. Sadly, this also strips out accented characters
    and non-Roman alphabetic characters.
    """

    # Scan the word for a-z or ' characters.
    convertedWord = "";
    for c in word:
        if 'A' <= c and  c <= 'Z':
            c = c.lower()
        if ('a' <= c and c <= 'z') or c == '\'':
            convertedWord += c;

    # If we added any such characters, return that word.
    if len(convertedWord) > 0:
        return convertedWord
    else:
        # Otherwise, return None.
        return None

def readWordsFromInput():
    """Returns the contents of console input as a list of words.

    Process the console input as consisting of lines of words. Return
    a list of all the words along with the strings that are "stoppers."
    Each non-stopper word in the list will be lowercase consisting only
    of the letters 'a'-'z' and also apostrophe. All other characters are
    stripped from the input. Stopper words are specified by the variable
    STOPPERS.
    """

    def spacedAround(text,c):
        """Returns modified text with spaces around any occurrence of c.

        Helper function that replaces any string `text` that has the
        character `c` so that all the occurrences of `c` are replaced
        with the substring " c ".
        """

        splits = text.split(c)
        return (" "+c+" ").join(splits)

    def spaceInsteadOf(text,c):
        """Returns modified text with space replacing any c.

        Helper function that replaces any string `text` that has the
        character `c` so that all the occurrences of `c` are replaced
        with a space.
        """

        splits = text.split(c)
        return (" ").join(splits)

    # Read the text into one (big) string.
    textChars = sys.stdin.read()

    # Add spaces around each "stopper" character.
    for stopper in STOPPERS:
        textChars = spacedAround(textChars,stopper)

    # Replace each whitespace character with a space.
    for character in WHITESPACE:
        textChars = spaceInsteadOf(textChars,character)

    # Split the text according to whitespace.
    rawWords = textChars.split(" ")

    # Process the raw words, simplifying them in the process by
    # skipping any characters that we don't currently handle.
    # We treat the "end of sentence"/"stopper" words specially,
    # including them in the list as their own strings.
    words = []
    for word in rawWords:
        if word not in STOPPERS:
            word = simplifyWord(word)
        if word is not None:
            words.append(word)
    return words


def train(theWords):
    """ Your comment goes here. """
    #my code
    train = {}
    slot=0

    #bigrams
    for j in theWords:
        if(slot<len(theWords)-1):
            nextWord=[theWords[slot+1]]
            if(theWords[slot] not in train):
                train[theWords[slot]]=nextWord
            else:
                train[theWords[slot]]+=nextWord
        slot+=1

    #trigrams
    slot=0
    for i in theWords:
        if(slot<len(theWords)-2):
            twoWords=theWords[slot]+' '+theWords[slot+1]
            nextWord=[theWords[slot+2]]
            if(twoWords not in train):
                train[twoWords]=nextWord
            else:
                train[twoWords]+=nextWord

        slot+=1
    return train
    #end my code

def chat(biTriDict,numLines,lineWidth):
    """ Your comment goes here. """
    #my code
    generatedText=[]
    i=0
    ranWord=''
    carry=0

    while(i<numLines):
        j=0
        while(j<lineWidth-1):
            j+=carry
            carry=0
            last= -1
            last2= -3

            if(len(generatedText)==0 or generatedText[last] not in biTriDict or generatedText[last]=='.'):
                ranWord=random.choice(biTriDict['.'])
            elif(len(generatedText)==1 or (generatedText[last2]+" "+generatedText[last]) not in biTriDict):
                prevWord=generatedText[last]
                ranWord=random.choice(biTriDict[prevWord])
            else:
                prevWord=generatedText[last]
                prevWord2=generatedText[last2]
                ranWord=random.choice(biTriDict[prevWord2+" "+prevWord])

            if(len(generatedText)!=0 and j+1+len(ranWord)<lineWidth-1):
                if(ranWord=='.'):
                    generatedText+=[ranWord]
                    j+=len(ranWord)
                else:
                    generatedText+= [' '] + [ranWord]
                    j+=1+len(ranWord)
            elif(len(generatedText)==0):
                generatedText+= [ranWord]
                j+=len(ranWord)
            elif(i<numLines-1):
                generatedText+= ['\n'] + [ranWord]
                j+=1+len(ranWord)
                carry=len(ranWord)
            else:
                j+=1+len(ranWord)

        i+=1

    print(''.join(generatedText))
    #end my code

#
# The main script. This script does the following:
#
# * Processes a series of lines of text input into the console.
#      => The words of the text are put in the list `textWords`
#
# * Scans the text to compute statistics about bi-grams and tri-
# grams that occur in the text. This uses the function `train`.
#
# • Generates a random text from the bi-/tri-gram dictionary
#   using a stochastic process. This uses the procedure 'chat'.
#

if __name__ == "__main__":

    # Read the words of a text (including ".", "!", and "?") into a list.
    print("READING text from STDIN. Hit ctrl-d when done entering text.")
    textWords = readWordsFromInput()
    print("DONE.")

    # Process the words, computing a dictionary.
    biTriDict = train(textWords)
    chat(biTriDict, 30, 70)
