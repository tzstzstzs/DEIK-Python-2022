
def decToBin(n):
    bin = []
    while n >= 1:
        bin.append(str(n % 2)) # n maradékosztás (1 vagy 0) -> stringgé alakítja -> beteszi a lista végére
        n //= 2
    bin = ''.join(bin)[::-1] # a bin listát egy stringgé alakítja és megfordítja.
    return bin
        

def main():
    print(decToBin(156))

##############################################################################

if __name__ == "__main__":
    main()
