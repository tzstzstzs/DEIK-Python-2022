

def hangrend(word):
    melyMgh = "aáoóuú"
    magasMgh = "eéiíöőüű"

    mely = False
    magas = False

    for i in range(len(word)):
        if word[i] in melyMgh:
            mely = True
        
        elif word[i] in magasMgh:
            magas = True

        if mely and magas:
            return "vegyes"

    if mely and magas == False:
        return "mely"
    elif mely == False and magas:
        return "magas"
    elif mely == False and magas == False:
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
