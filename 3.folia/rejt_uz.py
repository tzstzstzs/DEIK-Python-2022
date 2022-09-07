
def decode(s):
    # s = s.replace('q', 'o').replace('y', 'a').replace('Y', 'A').replace('k', 'm').replace('e', 'g').replace('c', 'e').replace('C', 'E').replace('w', 'y')

    s = s.replace('m', 'k').replace('q', 'o').replace('g', 'e')

    return s



def main():
    uzenet = """
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb
    """
    print(decode(uzenet))
##############################################################################

if __name__ == "__main__":
    main()
