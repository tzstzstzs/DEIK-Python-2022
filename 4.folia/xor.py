

def xor(s1, s2):
    if (bool(s1) and bool(s2) == False) or (bool(s1) == False and bool(s2)):
        return True

    else:
        return False


def main():
    str1 = "python"
    str2 = None

    print(xor(str1, str2))

##############################################################################

if __name__ == "__main__":
    main()
