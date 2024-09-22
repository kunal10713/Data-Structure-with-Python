'''
      * 
    * * 
  * * * 
* * * * 
'''


row = 1
n = int(input())


while(row <= n):
    space = n - row
    while(space):
        print(" ", "", end="")
        space -= 1
    
    col = 1
    while( col <= row):
        print("*", "", end="")
        col += 1
    print()  
    row += 1