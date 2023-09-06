def topWordExcept(freqs,excluded):
    """Gets the most frequent word in a dictionary that's not excluded.

    Find the most frequently occurring word in a text, excluding any
    words that are in the list `excluded`. The text is summarized by a
    word frequency dictionary `freqs`. If there are no words except
    the excluded ones, this function returns the value `None`.

    Example:
    >>> wf = wordFrequencies(["hello", "there", ".", "hello", "!"])
    >>> topWordExcept(wf,[])
    'hello'
    >>> topWordExcept(wf,['hello'])
    'there'
    >>> print(topWordExcept(wf,['hello','there']))
    None

    """
    #my code
    top=0
    topName=''
    if(len(excluded)>0):
        for i in freqs:
            for j in excluded:
                if(freqs[i]>top and i!=j):
                    top=freqs[i]
                    topName=i
    else:
        for i in freqs:
            if(freqs[i]>=top):
                top=freqs[i]
                topName=i

    if(len(freqs) != 0):
        return topName
    else:
        return None
