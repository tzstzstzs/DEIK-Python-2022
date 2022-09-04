
def lista_szorzata(li):
    sz = 1
    for e in li:
        sz *= e
    return sz


def szamjegyek_sum(li):
    sum = [str(e) for e in li]

    return len(''.join(sum))


def main():
    li = [3, 5, 10, 4, 2]
    print(lista_szorzata(li))
    print(szamjegyek_sum(li))


##############################################################################


if __name__ == "__main__":
    main()
