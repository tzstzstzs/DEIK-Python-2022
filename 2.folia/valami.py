import sys
from tkinter import N, Y


def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    # if inp == 'y' or inp == 'Y' or inp == 'yes':    # <- egyszerűbben?
    a = inp[0].lower()
    if a == 'y':
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')

##############################################################################

if __name__ == "__main__":
    main()
