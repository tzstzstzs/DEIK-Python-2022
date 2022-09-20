

def normalize(text):
    return text.lower().replace(' ', '')


def stringToList(text):
    text = normalize(text)
    li = []
    for i in range(len(text)):
        li.append(text[i])
    return li


def listToDict(text):
    li = stringToList(text)
    d = {}
    for c in li:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def main():
    dict1 = listToDict("A gentleman")
    dict2 = listToDict("Elegant man")
    print("True" if dict1 == dict2 else "False")

##############################################################################

if __name__ == "__main__":
    main()
