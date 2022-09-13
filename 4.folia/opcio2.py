

from turtle import pos


def hello(name, repeat=1, postfix=''):
    for i in range(repeat):
        print(name + postfix)


def main():
    hello("Joe")
    hello("Jane", repeat=3)
    hello("Julia", repeat=5, postfix='!')
    hello("Janet", 2, '?')

##############################################################################

if __name__ == "__main__":
    main()
