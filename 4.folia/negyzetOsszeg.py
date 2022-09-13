

def negyzetOsszeg(n):
    sum = 0
    for i in range(n):
        sum = sum + (i + 1) ** 2

    return sum


def osszegNegyzet(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    sum = sum ** 2

    return sum


def main():
    print(negyzetOsszeg(10))
    print(osszegNegyzet(10))

##############################################################################

if __name__ == "__main__":
    main()
