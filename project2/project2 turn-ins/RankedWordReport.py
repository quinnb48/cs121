def rankedWordReport(ranking,topWordsList,freqs):
    """ Returns a string reporting a ranking of word occurrences.

    When a text has been summarized with the dictionary `freqs`,
    giving the words in it, and their number of occurrences, and
    then that dictionary has been distilled to the most frequently
    occurring words as a list `topWordsList`, ordered from most-
    to least-frequent, then this function returns a string
    giving the information about a word of rank `ranking`.

    The format of the string should be the ranking, followed by
    a period, followed by a space, followed by the word, followed
    by a colon character, followed by the number of occurrences
    of that word.

    Suppose, for example, that the word "the" is the most frequent
    word in a text, and it occurs 12345 times. Then calling this
    function with `ranking == 1` will return the string

        "1. the:1235"

    This would also mean that

        `topWordsList[0] == "the" and freqs["the"] == 1235`

    """
    #my code
    num = str(ranking)
    word = str(topWordsList[ranking-1])
    frequent= str(freqs[word])

    return num + ". " + word + ":" + frequent
