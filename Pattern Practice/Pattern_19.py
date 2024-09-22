
'''

1 2 3 4 5 5 4 3 2 1
1 2 3 4 * * 4 3 2 1
1 2 3 * * * * 3 2 1
1 2 * * * * * * 2 1
1 * * * * * * * * 1

'''

'''
Let's break down the logic for all three triangles in brief:

1. First Triangle (Left-side Numbers):
This triangle prints numbers in increasing order from 1 to start, where start = n - row + 1 (i.e., the number of values decreases with each row).

Logic:
For each row, the numbers printed on the left start at 1 and go up to start, which is calculated as n - row + 1 
(this ensures that the first row prints n numbers, the second row prints n-1 numbers, and so on).

Example for n = 5:

Row 1: 1 2 3 4 5
Row 2: 1 2 3 4
Row 3: 1 2 3
Row 4: 1 2
Row 5: 1


2. Second Triangle (Asterisks *):
The second triangle is made up of asterisks (*), and the number of asterisks increases with each row. 
It adds symmetry to the pattern by replacing where numbers would have been on the left.

Logic:

The number of asterisks (*) in each row is 2 * (row - 1) 
(this ensures that the first row has 0 asterisks, the second row has 2 asterisks, and so on).

Example for n = 5:

Row 1: (no asterisks)
Row 2: * *
Row 3: * * * *
Row 4: * * * * * *
Row 5: * * * * * * * *

3. Third Triangle (Right-side Numbers):
This triangle mirrors the first triangle. It prints numbers in decreasing order starting from start down to 1.

Logic:
After printing the asterisks, the right-side numbers are the same as the left-side numbers but printed in reverse order. 
For each row, it starts at start and decrements down to 1.

Example for n = 5:

Row 1: 5 4 3 2 1
Row 2: 4 3 2 1
Row 3: 3 2 1
Row 4: 2 1
Row 5: 1


Summary of All Three Triangles:
- First Triangle (Left-side): Numbers are printed from 1 to start (where start decreases as the row number increases).
- Second Triangle (Middle Asterisks): Asterisks (*) are printed in the middle, increasing by 2 per row.
- Third Triangle (Right-side): Numbers are printed in reverse order from start down to 1, creating a mirror image of the first triangle.

'''


row = 1
n = int(input())

while row <= n:
    # Print the decreasing numbers in the first triangle
    col = 1
    start = n - row + 1
    while col <= start:
        print(col, "", end="")
        col += 1

    # Print the asterisks in the second triangle
    num_stars = 2 * (row - 1)
    while num_stars > 0:
        print("*", "", end="")
        num_stars -= 1

    # Print the decreasing numbers on the right side
    col = start
    while col:
        print(col, "", end="")
        col -= 1

    print()
    row += 1