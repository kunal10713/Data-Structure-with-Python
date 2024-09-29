# Prompt the user to input a decimal number to convert to binary
n = int(input("Enter a number to convert from decimal to binary: "))

# Initialize 'binary_num' to store the binary representation of the decimal number
binary_num = 0

# Initialize 'i' as the position index to track the place value of the binary digits
i = 0

# Continue the loop until 'n' becomes 0
while n != 0:
    last_bit = n & 1  # Use bitwise AND to get the least significant bit (LSB) of 'n'
    
    # Construct the binary number by adding the last bit to the correct place value
    binary_num = (last_bit * pow(10, i)) + binary_num
    
    # This logic can also be used to reverse a number if instead of the last digit, we start with the first digit of the number.
    # In that case, we would construct the reverse number by extracting the first digit and building the reversed number from left to right.

    
    # Right-shift 'n' by 1 to remove the least significant bit, i.e., divide by 2
    n = n >> 1

    # Increment 'i' to move to the next place value in the binary representation
    i += 1


# Print the final binary representation of the input decimal number
print(f"Binary number: {binary_num}")