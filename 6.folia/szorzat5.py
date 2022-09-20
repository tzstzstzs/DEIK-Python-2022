

def removeenter(text):
    return text.replace('\n', '')


def sliceTextToInt(text):
    li = []
    for i in range(len(text)):
        a = text[i]
        if a.isspace():
            continue
        a = int(a)
        li.append(a)
    return li


def szorzat5(li):
    szorzatLista = []
    for i in range(len(li)-4):
        n = li[i] * li[i+1] * li[i+2] * li[i+3] * li[i+4]
        szorzatLista.append(n)
    return max(szorzatLista)


def szorzatWithZip(li):
    otosLista = list(zip(li, li[1:], li[2:], li[3:], li[4:]))
    szorzatLista = []
    for elem in otosLista:
        product = elem[0] * elem[1] * elem[2] * elem[3] * elem[4]
        szorzatLista.append(product)
    return max(szorzatLista)



def main():
    with open("6.folia/szamok2.txt", 'r') as f:
        text = f.read()

    print(szorzat5(sliceTextToInt(removeenter(text))))
    print(szorzatWithZip(sliceTextToInt(removeenter(text))))
##############################################################################

if __name__ == "__main__":
    main()
