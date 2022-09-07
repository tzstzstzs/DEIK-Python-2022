"""
Állapítsuk meg azon 1000-nél kisebb számok összegét, melyek 3-nak vagy 5-nek a többszörösei.
Oldjuk meg a problémát egy (azaz 1) sorban list comprehension segítségével. Tipp: használjuk a sum beépített függvényt.
"""

import math


def kisebb_egesz_3_5_kt(n):
    """
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s
    """
    s = [e for e in range(1, n) if e % 3 == 0 or e % 5 == 0]

    return sum(s)


def main():
    print(kisebb_egesz_3_5_kt(1000))

##############################################################################

if __name__ == "__main__":
    main()
