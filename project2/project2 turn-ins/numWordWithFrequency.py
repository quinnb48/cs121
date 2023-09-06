def numWordsWithFrequency(freqDict,freq):
    """ Return how many words occur some number of times in a text.

    Given a word frequence dictionary `freqDict` and a number of
    occurrences `freq`, this function returns how many words in
    the dictionary have that count of occurrences.
    """
    #my code
    howManyWords = 0

    for i in freqDict:
        if(freqDict[i] == freq):
            howManyWords+=1

    return howManyWords
