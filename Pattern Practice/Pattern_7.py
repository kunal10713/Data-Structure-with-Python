'''
1 
2 3 
4 5 6 

'''

row = 0
n = int(input())

while (row <= n):
    col = 1
    while(col <= row ):
        print((row * (row - 1)) // 2 + col, "", end="")
        col += 1
    '''
    To generalize, the first number of any row r is the sum of numbers in all the previous row
    Row 1 has 1 number.
    Row 2 has 2 numbers.
    Row 3 has 3 numbers.
    Row 4 has 4 numbers.
    
    The sum of the first r-1 rows is given by the sum of the first r-1 integers: (r x (r-1))/2)
    
    '''
    print()
    row += 1
    