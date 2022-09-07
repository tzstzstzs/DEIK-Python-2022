
def print_ASCII():
    for i in range(32, 128):
        print("{}: {}".format(i, chr(i)))
    return


def capital_sum():
    print(sum(range(65, 91)))
    return



def main():
    print_ASCII()
    capital_sum()

##############################################################################

if __name__ == "__main__":
    main()
