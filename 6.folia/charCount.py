

def stringToCharlist(text):
    li = []
    for i in range(len(text)):
        a = text[i]
        if a.isspace():
            li.append('whitespace')
            continue
        elif a.isalpha():
            li.append(a)
        else:
            li.append('other')
    return li


def charCount(text):
    list = stringToCharlist(text)
    d = {}
    for c in list:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    # d['whitespace'] = d.pop(' ')
    return sorted(d.items())
            

def main():
    print(charCount('cat and dog...'))
    print('END')
    

##############################################################################

if __name__ == "__main__":
    main()
