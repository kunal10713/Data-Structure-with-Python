'''
A 
B C 
C D E 
D E F G
'''


row = 1
n = int(input())
ch = 65



while(row <= n):
    col = 1
    while(col <= row):
        print(chr(ch + row + col - 2), "", end="")
        col += 1
    print()   
    row += 1
