

def diamond(n):
    if n % 2 == 0:
        print("Error! Odd number needed.")
    else:
        i = 1
        while i:
            star = '*' * i
            print(star.center(n))
            i += 2
            if i > n:
                break

        i = n - 2
        while i:
            star = '*' * i
            print(star.center(n))
            i -= 2
            if i < 1:
                break



def main():
    diamond(7)

##############################################################################

if __name__ == "__main__":
    main()
