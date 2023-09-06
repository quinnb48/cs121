def topWordsByFrequency(freqs,howMany):
    """Return the top occurring words in a text.

    Return a list of the most frequently occurring words in a text.
    The text is summarized by a word frequency dictionary `freqs`.
    The length of the list of the top-occurring words is dictated by
    the value of `howMany`. E.g. if `howMany == 3` then only the three most
    frequently occurring words should be in that list.

    Example:
    >>> wf = wordFrequencies(["hello", "there", ".", "hello", "!"])
    >>> topWordsByFrequeny(wf,1)
    ['hello']
    >>> topWordsByFrequency(wf,2)
    ['hello', 'there']

    The list of words should be in order of the most frequent to the
    least frequent. If there are several ties for what could be the
    top `howMany`-th most-frequent words, this code can choose any
    of those with equal frequency. For example:

    >>> wf = wordFrequencies(["hello", "there", "goodbye", "abe"])
    >>> twbf = topWordsByFrequency(wf,2)

    Then in the above, `twbf` could contain `hello` and `there`,
    or `hello` and `abe`, or `goodbye` and `there`, etc. Any two
    of those four words are the top two most-frequent words.

    """
    #my code
    top=['']*howMany
    topNum=[0]*howMany
    i=0

    while(i<len(topNum)):
        for j in freqs:
            if (freqs[j]>=topNum[i] and j not in top):
                top[i]=j
                topNum[i]=freqs[j]
        i+=1

    return top
