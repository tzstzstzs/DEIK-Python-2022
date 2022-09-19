

# INPUT = "szamok.txt"


def main():
    f = open("szamok.txt", 'r')

    lista = f.read().splitlines()

    f.close()

    osszeg = 0

    for nr in lista:
        osszeg += int(nr)

    print(str(osszeg)[:10])
##############################################################################

if __name__ == "__main__":
    main()
