


row = 1
n = int(input())

while(row <=n):
    col = 1
    while(col <= row):
        print(row - col + 1, "" , end="")
        col += 1
    print()
    row += 1
