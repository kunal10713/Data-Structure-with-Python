'''
1  2  3  
4  5  6  
7  8  9
'''


i = 1
n = int(input())
count = 1

while (i <= n):
    j = 1
    while(j <= n):
        print(count, " ", end="")
        j += 1 
        count += 1  
    print()
    i += 1
    
         