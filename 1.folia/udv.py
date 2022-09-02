"""
    udv.py Batman -> Denevérveszély

    UDV.PY zSOLTI -> Hello Zsolti!
"""


import sys


def hello(nev):
    if nev == 'Batman':
        print("Denevérveszély")
    else:
        print("Hello " + nev + "!")


def main():
    name = sys.argv[1]
    hello(name)

##############################################################################

if __name__ == "__main__":
    main()
