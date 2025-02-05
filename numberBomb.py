#! python3

import os
import random

l, r = 1, 100
flag, isLegal = True, False

bomb = random.randint(l + 1, r - 1)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    global l, r, flag, isLegal, bomb
    while flag:
        print('Please input a number which between %d and %d' % (l, r))
        isLegal = False
        while not isLegal:
            try:
                val = int(input())
                isLegal = True
            except ValueError:
                print('Please input an integer\nTry it again')
            if not (l < val < r):
                print('Please input an integer between %d and %d\nTry it again' % (l, r))
                isLegal = False
        if val == bomb:
            print('This is bomb\nyou lose')
            flag = False
        elif val < bomb:
            l = val
        else:
            r = val
        if r - l == 2:
            print('The range is (%d, %d), the bomb is %d\nyou win' % (l, r, bomb))
            flag = False
        if flag:
            os.system('pause')
            clear_screen()

if __name__ == '__main__':
    main()
