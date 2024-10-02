def fibonacci(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 3

    while count < num:
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    
    print(next_number)
    
# Input for nth place
n = int(input("Enter the first number: "))

fibonacci(n)



