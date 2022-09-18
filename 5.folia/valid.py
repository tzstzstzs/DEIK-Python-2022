

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    li = []
    res = ''
    for i in range(len(text)):
        if text[i] in chars:
            li.append(text[i])
    res = ''.join(li)
    return res
    """

    return ''.join(text[i] for i in range(len(text)) if text[i] in chars)


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))

##############################################################################


if __name__ == "__main__":
    main()
