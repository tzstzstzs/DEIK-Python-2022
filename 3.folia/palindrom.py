
def isPalindrome(t):
    t = t.lower().replace(' ', '').replace('.', '').replace(',', '')

    if t == t[::-1]:
        return True

    else:
        return False


def isPalindromeIt(t):
    t = t.lower().replace(' ', '').replace('.', '').replace(',', '')
    i = 0
    while i < len(t) / 2:
        if t[i] != t[-1 - i]:
            return False
        i += 1
    return True


def main():
    s = "Eva, can I see bees in a cave"
    print(isPalindrome(s))
    print(isPalindromeIt(s))

##############################################################################

if __name__ == "__main__":
    main()
