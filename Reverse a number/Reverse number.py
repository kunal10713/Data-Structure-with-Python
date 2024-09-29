# Prompt the user to input a number to find its reverse
n = int(input("Enter a number to find its reverse: "))

# Initialize the variable 'reverse' to store the reversed number
reverse = 0

# Continue the loop until 'n' becomes 0
while n != 0:
    last = n % 10  # Get the last digit of the number using modulus
    reverse = (reverse * 10) + last  # Append the last digit to the 'reverse' variable
    n = n // 10  # Remove the last digit from 'n' by doing an integer division by 10

# Print the reversed number
print(f"Reversed number: {reverse}")