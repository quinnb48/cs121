def wordCount(freqs):
    """Returns the word count and vocabulary size of a text.

    Given a dictionary of words and their frequency of occurrence,
    computed from a text, return the total number of words that occurred
    in the original text (counting repetions of words) along with the
    number of distinct words that appeared in that text.

    Example:
    >>> wf = wordFrequencies(["hello", "there", ".", "hello", "!"])
    >>> count,vocabSize = wordCount(wf)
    >>> print(count,vocabSize)
    3,2

    NOTE: this function returns a pair. The first component of the
    pair should is the size of the text in # of words. The second
    component of the pair is the # of distinct words.

    """
    #my code
    numWords=0
    numDiffWords=0
    for i in freqs:
        numWords+=freqs[i]
        numDiffWords+=1

    return numWords,numDiffWords
