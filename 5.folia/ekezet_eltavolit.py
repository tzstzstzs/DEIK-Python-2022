

def ekezetLe(str):
    res = str.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ö', 'o').replace('ő', 'o').replace('ú', 'u').replace('ü', 'u').replace('ű', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ö', 'O').replace('Ő', 'O').replace('Ú', 'U').replace('Ü', 'U').replace('Ű', 'U')
    return res


def ekezetLeSzotar(str):
    d = {'á': 'a', }


def main():
    TEXT = """
    A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

    A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

    A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
    """

    print(ekezetLe(TEXT))

##############################################################################

if __name__ == "__main__":
    main()
