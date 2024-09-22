
'''
A B C 
A B C 
A B C 
'''

row = 1
n = int(input())
ch = 65



while(row <= n):
    col = 1
    while(col <= n):
        print(chr(ch + col - 1), "", end="")
        col += 1
    print()   
    row += 1