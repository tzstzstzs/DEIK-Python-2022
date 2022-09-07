
def lista_szorzata(li):
    sz = 1
    for e in li:
        sz *= e
    return sz


def szamjegyek_darab_sum(li):
    sum = [str(e) for e in li]
    return len(''.join(sum))


def szamjegyek_összege(li):
    """
    # sztringgé alakítja az int listát és egyesíti
    # az egyesített sztring minden karakterét integerré alakítja és összeadja.
    """
    a = ''.join([str(e) for e in li]) 
    sum = 0
    for i in range(len(a)): 
        sum += int(a[i])
    return sum


def main():
    li = [3, 5, 10, 4, 2]
    print(lista_szorzata(li))
    print(szamjegyek_darab_sum(li))
    print(szamjegyek_összege(li))


##############################################################################


if __name__ == "__main__":
    main()
