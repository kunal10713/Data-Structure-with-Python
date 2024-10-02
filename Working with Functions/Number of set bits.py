def set_bits_in_two_numbers(num1, num2):
    # Function to count set bits for a single number
    def count_set_bits(num):
        set_bit_count = 0
        while num != 0:
            if num & 1:
                set_bit_count += 1
            num = num >> 1
        return set_bit_count

    # Calculate set bits for both numbers
    set_bits_a = count_set_bits(num1)
    set_bits_b = count_set_bits(num2)

    return set_bits_a, set_bits_b

# Input for both numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the function and get the set bit counts for both numbers
set_bits_a, set_bits_b = set_bits_in_two_numbers(a, b)

# Print the result for both numbers
print(f"Set bits in {a}: {set_bits_a}")
print(f"Set bits in {b}: {set_bits_b}")
