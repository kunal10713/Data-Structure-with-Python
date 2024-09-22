
'''
A B C
B C D 
C D E 
'''

row = 1
n = int(input())
ch = 65



while(row <= n):
    col = 1
    while(col <= n):
        print(chr(ch + row + col - 2), "", end="")
        col += 1
    print()   
    row += 1