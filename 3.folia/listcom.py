
from ntpath import join
from posixpath import split
from unittest import result


def f1():
    li = ['auto', 'villamos', 'metro']
    result = [word.upper() + '!' for word in li]
    print(result)

def f2():
    li = ['aladar', 'bela', 'cecil']
    result = [word.capitalize() for word in li]
    print(result)


def f3():
    res = [0 for i in range(10)]
    print(res)


def f4():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = [n * 2 for n in li]
    print(res)


def f5():
    li =['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    res = [int(n) for n in li]
    print(res)


def f6():
    sztr = '1234567'
    res = [int(sztr[e]) for e in range(len(sztr))]
    print(res)


def f7():
    sentence = "The quick brown fox jumps over the lazy dog"
    li = sentence.split()
    res = [len(li[e]) for e in range(len(li))]
    print(res)


def f8():
    sentence = "python is an awesome language"
    li = sentence.split()
    res = [word[0] for word in li]
    print(res)


def f9():
    sentence = "The quick brown fox jumps over the lazy dog"
    li = [(word, len(word)) for word in sentence.split()]
    print(li)


def f10():
    res = [n for n in range(10) if n % 2 ==0]
    print(res)


def f11():
    res = [n * n for n in range(20) if n % 2 == 0]
    print(res)


def f12():
    res = [n * n for n in range(20) if n * n % 10 == 4]
    print(res)


def f13():
    res = ''.join([chr(e) for e in range(65, 91)])
    print(res)


def f14():
    li = [' apple ', ' banana ', ' kiwi']
    res = [word.replace(' ', '') for word in li]
    print(res)


def f15():
    li = [1, 0, 1, 1, 0, 1, 0, 0]
    res = ''.join([str(n) for n in li])
    print(res)
    

def main():
    f1()
    print('-' * 40)
    f2()
    print('-' * 40)
    f3()
    print('-' * 40)
    f4()
    print('-' * 40)
    f5()
    print('-' * 40)
    f6()
    print('-' * 40)
    f7()
    print('-' * 40)
    f8()
    print('-' * 40)
    f9()
    print('-' * 40)
    f10()
    print('-' * 40)
    f11()
    print('-' * 40)
    f12()
    print('-' * 40)
    f13()
    print('-' * 40)
    f14()
    print('-' * 40)
    f15()
    print('-' * 40)

##############################################################################

if __name__ == "__main__":
    main()
