# Prompt the user to input a binary number to convert to decimal
n = int(input("Enter a number to convert from binary to decimal: "))

# Initialize 'decimal_num' to store the decimal representation of the binary number
decimal_num = 0

# Initialize 'i' as the position index to track the place value of the binary digits
i = 0

# Continue the loop until 'n' becomes 0
while n != 0:
    # Get the last digit of the binary number using modulus operator
        # Question: Why not last_bit = n & 1?
        # Answer: `n % 10` extracts the last digit of the binary number in decimal form (i.e., 0 or 1),
        # whereas `n & 1` extracts the least significant bit of the number in its binary representation.
        # Since we are iterating over the decimal representation of the binary number (e.g., 101 in decimal), 
        # `n % 10` is appropriate for extracting each digit one by one.

    last_bit = n % 10
    
    # Check if the last bit is 1 (i.e., the binary digit is set)
    if last_bit & 1 == 1:
        # Add the corresponding power of 2 based on the digit's position index 'i'
        decimal_num = decimal_num + pow(2, i)
    
    # Remove the last digit from 'n' by dividing by 10 (integer division)
        # Question: Why not n = n >> 1?
        # Answer: `n = n // 10` removes the last digit of the decimal representation of the binary number,
        # whereas `n = n >> 1` performs a right-shift operation on the binary representation itself.
        # Since we are working with a decimal form of the binary number (e.g., input `101` as decimal), `n // 10` is suitable.

    n = n // 10
    
    # Increment 'i' to move to the next place value in the binary representation
    i += 1

# Print the final decimal representation of the input binary number
print(f"Decimal number: {decimal_num}")
