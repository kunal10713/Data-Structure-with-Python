'''
* * * * 
* * * 
* * 
*  
'''


row = 1
n = int(input())


while(row <= n):
    col = 1
    start = n - row + 1
    while(start):
        print("*", "", end="")
        col += 1
        start -= 1
    print()  
    row += 1