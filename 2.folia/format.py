
PI = 3.14

def hello(name, color, obj):
     #1
     print("{0}, {1} az {2}! Ki? {0}".format(name, color, obj))
     #2
     print("{}, {} az {} eg!".format(name, color, obj))
     #3
     print("{n}, {c} az {o}!".format(n=name.capitalize(), c=color, o=obj))
     #4
     print(f"{name}, {color} az {obj}!")


def main():
    hello("geza", "kek", "eg")
    print("-" * 40)
    hello("peti", "piros", "auto")
    print("-" * 40)
    print(f"pi erteke: {PI}")
    print("pi erteke: ", PI)

##############################################################################

if __name__ == "__main__":
    main()
