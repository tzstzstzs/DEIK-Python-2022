def is_palindrom(t):
    t = t.lower()
    t = t.replace(' ', '')
    t = t.replace('.', '')
    t = t.replace(',', '')

    if t == t[::-1]:
        return True

    else:
        return False


def main():
    t = "Eva, can I see bees in a cave"
    print(is_palindrom(t))

##############################################################################

if __name__ == "__main__":
    main()
