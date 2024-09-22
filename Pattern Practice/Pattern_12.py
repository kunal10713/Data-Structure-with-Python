'''
A 
B B 
C C C 
'''


row = 1
n = int(input())
ch = 65



while(row <= n):
    col = 1
    while(col <= row):
        print(chr(ch + row - 1), "", end="")
        col += 1
    print()   
    row += 1