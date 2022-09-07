
def remove_spaces(text):
    return text.replace(' ', '').replace('\n', '')


def main():
    szoveg = """   Ez egy
    proba
    """
    print(remove_spaces(szoveg))

##############################################################################

if __name__ == "__main__":
    main()
