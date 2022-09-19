

INPUT = "szoveg.txt"
OUTPUT = "masolat.txt"


def main():
    with open(INPUT, 'r') as f1, open(OUTPUT, 'w') as to:
        for line in f1:
            to.write(line)
    print("END")

##############################################################################

if __name__ == "__main__":
    main()
