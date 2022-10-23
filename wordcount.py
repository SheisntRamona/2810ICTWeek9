import sys
import string

def f1(file):
    fhand = open(file)
    counts = {}
    words = fhand.read().split()

    if len(words) == 0:
        fhand.close()
    else:
        for word in words:
            translator = str.maketrans('', '', string.punctuation)
            w = word.upper().translate(translator)
            if (len(w) > 0):
                counts[w] = counts.get(w, 0) + 1
        fhand.close()

    return counts

def f2(dictionary):
    if len(dictionary) != 0:
        lst = []
        for key, val in dictionary.items():
            newtup = (val, key)
            lst.append(newtup)
            lst = sorted(lst, reverse=True)

    return lst