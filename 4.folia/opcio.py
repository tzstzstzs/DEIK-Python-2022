

def hello(name, greetings="Hello"):
    print(f"{greetings} {name}!")


def main():
    hello("Zsolti")
    hello("Zsolti", "Bonjour")
    hello("Zsolti", greetings="Hola")

##############################################################################

if __name__ == "__main__":
    main()
