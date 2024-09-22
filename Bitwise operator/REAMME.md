# Bitwise Operator and Explaination 

## Python code in file Bitwise_explaination.py


# Variables:
a = 4: In binary, 4 is represented as 0100.
b = 6: In binary, 6 is represented as 0110.
The code applies various bitwise operations to these values.

1. Bitwise AND Operator (&):
The AND operator compares each bit of two numbers. It returns 1 only if both corresponding bits are 1; otherwise, it returns 0.
a & b compares the binary values of a and b:
css
Copy code
a = 4   ->  0100
b = 6   ->  0110
----------------
a & b   ->  0100   (result is 4 in decimal)
Output: AND operator a & b --> 4


2. Bitwise OR Operator (|):
The OR operator compares each bit of two numbers. It returns 1 if either of the corresponding bits is 1; if both bits are 0, it returns 0.
a | b compares the binary values of a and b:
css
Copy code
a = 4   ->  0100
b = 6   ->  0110
----------------
a | b   ->  0110   (result is 6 in decimal)
Output: OR operator a | b --> 6



3. Bitwise NOT Operator (~):
The NOT operator flips all bits of the number. In Python, the bitwise NOT operation is also equivalent to -(n+1) for any integer n.

~a flips the bits of a (4), which is 0100 in binary:


a = 4   ->  0100
~a      ->  1011   (which is -5 in decimal, because Python stores integers using two's complement form)
Output: NOT operator ~a --> -5

Example: Calculating Two's Complement for a 4-bit number 4 (which is 0100):
Let's compute the two's complement of 4 to represent -4:

Start with the binary representation of 4 (positive):

4 (decimal)  = 0100 (binary)

Invert all bits:
0100 --> 1011

Add 1:

1011 + 1 = 1100

Thus, the two's complement of 4 is 1100, which represents -4 in a 4-bit signed system.


Similarly, ~b flips the bits of b (6), which is 0110 in binary:


b = 6   ->  0110
~b      ->  1001   (which is -7 in decimal)
Output: NOT operator ~b --> -7

4. Bitwise XOR Operator (^):
The XOR operator compares each bit of two numbers. It returns 1 if only one of the corresponding bits is 1; if both bits are the same, it returns 0.
a ^ b compares the binary values of a and b:


a = 4   ->  0100
b = 6   ->  0110
----------------
a ^ b   ->  0010   (result is 2 in decimal)

Output: XOR operator a ^ b --> 2
