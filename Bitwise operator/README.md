# Bitwise Operators and Explanation

## Python Code in File `Bitwise_explanation.py`

This Python code demonstrates the behavior of various bitwise operators applied to two integer values `a = 4` and `b = 6`.

### Variables:
- `a = 4`: In binary, 4 is represented as `0100`.
- `b = 6`: In binary, 6 is represented as `0110`.

The code applies various bitwise operations to these values, which are detailed below:

---

### 1. Bitwise AND Operator (`&`):
The **AND operator** compares each bit of two numbers. It returns `1` only if both corresponding bits are `1`; otherwise, it returns `0`.

**Binary Representation**:

a = 4 -> 0100 b = 6 -> 0110
a & b -> 0100 (result is 4 in decimal)

**Output**: `AND operator a & b --> 4`

---

### 2. Bitwise OR Operator (`|`):
The **OR operator** compares each bit of two numbers. It returns `1` if **either** of the corresponding bits is `1`; if both bits are `0`, it returns `0`.

**Binary Representation**:

a = 4 -> 0100 b = 6 -> 0110
a | b -> 0110 (result is 6 in decimal)
**Output**: `OR operator a | b --> 6`

---

### 3. Bitwise NOT Operator (`~`):
The **NOT operator** flips all bits of the number. In Python, the bitwise NOT operation is equivalent to `-(n + 1)` for any integer `n`.

- **NOT operation on `a = 4`**:
a = 4 -> 0100 
~a -> 1011 (which is -5 in decimal, because Python stores integers using two's complement form)

**Output**: `NOT operator ~a --> -5`

- **NOT operation on `b = 6`**:

b = 6 -> 0110 
~b -> 1001 (which is -7 in decimal)

**Output**: `NOT operator ~b --> -7`

---

#### Example: Calculating Two's Complement for a 4-bit Number `4` (`0100`):

To compute the two's complement of `4` to represent `-4`:

1. **Start with the binary representation of 4**:

4 (decimal) = 0100 (binary)

2. **Invert all bits**:
0100 --> 1011

3. **Add 1**:
1011 + 1 = 1100

Thus, the two's complement of `4` is `1100`, which represents `-4` in a 4-bit signed system.

---

### 4. Bitwise XOR Operator (`^`):
The **XOR operator** compares each bit of two numbers. It returns `1` if **only one** of the corresponding bits is `1`; if both bits are the same, it returns `0`.

**Binary Representation**:
a = 4 -> 0100 b = 6 -> 0110
a ^ b -> 0010 (result is 2 in decimal)

**Output**: `XOR operator a ^ b --> 2`

## Instructions to Run the Code:
Save the code in a file named Bitwise_explanation.py.
Run the file using Python:
    python Bitwise_explanation.py
his will display the output for each bitwise operation as explained above.







