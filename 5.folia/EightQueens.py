

def eightQueens(list): # [7,3,0,2,5,1,6,4]
    print('+' + '-' * 17 + '+')
    for i in range(len(list)):
        print('|', end=' ')
        for j in list:
            if len(list) - 1 - j == i:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print('|')
    print('+' + '-' * 17 + '+')
    


def main():
    eightQueens([7,3,0,2,5,1,6,4])

##############################################################################

if __name__ == "__main__":
    main()
