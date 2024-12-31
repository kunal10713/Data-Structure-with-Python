# Bitwise Shift Operators with Padding Explanation

## Overview

This README provides details about Python's **bitwise shift operators** (`<<` and `>>`) and the concept of **padding** during these operations. We'll explore how these operators work and how padding is applied for positive numbers.

## Code File: `shift_operations.py`

This Python file demonstrates the behavior of left and right shift operations, showing how padding works during these shifts.

---

## 1. Left Shift Operator (`<<`)

The **left shift operator** shifts the bits of a number to the left by a specified number of positions. Each left shift operation **multiplies the number by 2** for each position shifted.

- **Padding Behavior**: During a left shift, bits are shifted to the left, and **0s are added** to the right.

### Example:
n = 5 -> 101 (binary) n << 1 -> 1010 (binary) = 10 (decimal)

Here, `0` is padded on the right during the shift.

---

## 2. Right Shift Operator (`>>`)

The **right shift operator** shifts the bits of a number to the right by a specified number of positions. Each right shift operation **divides the number by 2** for each position shifted.

- **Padding Behavior**: During a right shift, bits are shifted to the right, and **0s are added** to the left for positive numbers.

### Example:
n = 5 -> 101 (binary) n >> 1 -> 10 (binary) = 2 (decimal)
Here, `0` is padded on the left during the shift.

---

## 3. Concept of Padding

**Padding** refers to the process of adding bits to replace the bits that are moved during shift operations:

- **Left Shift (`<<`)**: Vacated positions on the right are always filled with `0s`.
- **Right Shift (`>>`)**: Vacated positions on the left are filled with `0s` for **positive numbers**.

For negative numbers, Python uses **two's complement** to represent them, and the behavior may vary.

---

## 4. Code Example: Left and Right Shift with Padding

```python
# Example to demonstrate padding in left and right shifts

n = 5  # Binary representation of 5 is 101

# Left Shift
left_shift = n << 1  # Shift left by 1 bit
# Expected: Padding with 0 on the right, result is 1010 (which is 10 in decimal)

# Right Shift
right_shift = n >> 1  # Shift right by 1 bit
# Expected: Padding with 0 on the left, result is 10 (which is 2 in decimal)

print("Original number (n):", n)
print("Binary of n:", bin(n))
print("After Left Shift (n << 1):", left_shift, "-> Binary:", bin(left_shift))
print("After Right Shift (n >> 1):", right_shift, "-> Binary:", bin(right_shift))

```

## Relationship Between Shift Operations and Powers of 2

Left Shift (<<): Shifting left by n bits is equivalent to multiplying the number by 2 power of n.

Right Shift (>>): Shifting right by n bits is equivalent to dividing the number by 2 power of n discarding any remainder.


