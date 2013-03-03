
def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    # open file and read words
    file = open(filename, "r")
    lines = map(lambda x: x.split(" "),file.readlines())
    import itertools
    merged = list(itertools.chain.from_iterable(lines))

    words = {}
    for word in merged:
        if words.has_key(word):
            words[word] += 1
        else:
            words[word] = 1

    sorted_words = sorted(words,key=words.get)
    
    listed = []
    for word in sorted_words:
        listed.insert(0,word)

    print listed[0:15]
    
    return

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    # open file and read words
    file = open(filename, "r")
    lines = map(lambda x: x.split(" "),file.readlines())
    import itertools
    merged = list(itertools.chain.from_iterable(lines))

    words = {}
    for word in merged:
        if words.has_key(word):
            words[word] += 1
        else:
            words[word] = 1

    sorted_words = sorted(words,key=words.get)
    
    listed = []
    for word in sorted_words:
        if len(word) >= min_chars:
            listed.insert(0,word)

    print listed[0:15]
    
    return

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    # open file and read words
    file = open(filename, "r")
    lines = map(lambda x: x.split(" "),file.readlines())
    import itertools
    merged = list(itertools.chain.from_iterable(lines))

    words = {}
    for word in merged:
        if words.has_key(word):
            words[word] += 1
        else:
            words[word] = 1

    sorted_words = sorted(words,key=words.get)
    
    listed = []
    for word in sorted_words:
        if len(word) >= min_chars:
            listed.insert(0,(words[word],word))

    print listed[0:15]
    
    return

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        # open file and read words
        file = open(filename, "r")
        lines = map(lambda x: x.split(" "),file.readlines())
        import itertools
        merged = list(itertools.chain.from_iterable(lines))

        words = {}
        for word in merged:
            if words.has_key(word):
                words[word] += 1
            else:
                words[word] = 1

        sorted_words = sorted(words,key=words.get)
        
        listed = []
        for word in sorted_words:
            if len(word) >= min_chars:
                listed.insert(0,(words[word],word))

        print listed[0:15]
        
    except IOError :
        print "File does not exist"

    return
