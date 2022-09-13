

from ctypes.wintypes import PINT


def loop(n, debug=False):
    if debug:
        print("# start loop")
        
    for i in range(1, n+1):
        print(i, end=' ')
    print('')
    
    if debug:
        print("# end loop")
    
    else:
        for i in range(n):
            print(i + 1, end=' ')


def main():
    loop(5, debug=True)

##############################################################################

if __name__ == "__main__":
    main()
