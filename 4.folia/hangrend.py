

import re


def hangrend(word):
    melyMgh = "aáoóuú"
    magasMgh = "eéiíöőüű"

    mely = 0
    magas = 0

    for i in range(len(word)):
        if word[i] in melyMgh:
            mely += 1
        
        elif word[i] in magasMgh:
            magas += 1

    if mely > 0 and magas == 0:
        return "mely"
    elif magas > 0 and mely == 0:
        return "magas"
    elif mely > 0 and magas > 0:
        return "vegyes"
    elif mely == 0 and magas == 0:
        return "semmilyen"


def testHangrend(words):
    for word in words:
        print("\"{}\" -> {}".format(word, hangrend(word)))


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pffff"]
    testHangrend(words)
    # print(hangrend("ablak"))

##############################################################################

if __name__ == "__main__":
    main()
