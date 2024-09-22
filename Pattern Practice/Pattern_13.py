'''
A 
B C 
D E F 
G H I J
'''

row = 1
n = int(input())
ch = 65



while(row <= n):
    col = 1
    while(col <= row):
        print(chr(ch), "", end="")
        col += 1
        ch += 1
    print()   
    row += 1
