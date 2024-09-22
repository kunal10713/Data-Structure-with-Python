'''
D 
C D 
B C D 
A B C D 
'''

row = 1
n = int(input())
ch = 65



while(row <= n):
    col = 1
    start = ch + n - row
    while(col <= row):
        print(chr(start), "", end="")
        col += 1
        start += 1
    print()  
    row += 1
 