

INPUT = "string1.py"
OUTPUT = "string1_clean.py"


def main():
    with open(INPUT, 'r') as f1, open(OUTPUT, 'w') as to:
        for line in f1:
            if line.startswith('#'):
                continue
            elif line.startswith('    #'):
                continue
            else:
                to.write(line)

    print('END')

##############################################################################

if __name__ == "__main__":
    main()
