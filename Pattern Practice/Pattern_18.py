'''
   1
  121
 12321
1234321
'''

row = 1
n = int(input())


while(row <= n):
    
    # print 1st triagngle with space
    col = 1 
    space = n - row
    while(space):
        print(" ", end="")
        space -= 1
        
    # print 2nd triagngle with numbers
    
    while(col <= row):
        print(col, end="")
        col += 1
    
    # print 3rd triagngle with numbers
    
    start = row - 1
    while(start):
        print(start, end="")
        start -= 1
    
    print()  
    row += 1
    