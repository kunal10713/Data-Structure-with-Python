'''
1 
2 2 
3 3 3 
'''



row = 0
n = int(input())


while (row <= n):
    col = 1
    while(col <= row ):
        print(row, "" , end="")
        col += 13
    
    print()
    row += 1
    
    