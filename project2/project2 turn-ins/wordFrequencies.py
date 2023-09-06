def wordFrequencies(wordList):
    """Return dictionary of the counts of words in of the given list.

    Given a list of strings that are either words or "stoppers", count
    the number of times each non-stopper word appears. Return a
    dictionary whose entries are the words and their number of
    occurrences.

    Example:
    >>> wf = wordFrequencies(["hello", "there", ".", "hello", "!"])
    >>> wf
    {'hello':2, 'there':1}

    """
    #my code
    freqs = {}
    slot=0
    for i in wordList:
        if(wordList[slot] != '!' and wordList[slot] != '.' and wordList[slot] != '?'):
            if(wordList[slot] not in freqs):
                freqs[i] = 1
            else:
                freqs[i] += 1
        slot+=1

    return freqs
