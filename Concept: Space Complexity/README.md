# Space Complexity

Space complexity is a concept in computer science that measures the amount of working storage an algorithm needs. It's a critical aspect to consider when analyzing algorithms, especially when working with large datasets or systems with limited memory.

## What is Space Complexity?

- **Definition**: Space complexity refers to the total amount of memory space required by an algorithm to execute as a function of the size of the input data. This includes both the space needed for input values and the space needed for auxiliary variables and data structures.

## Components of Space Complexity

Space complexity can be divided into two main components:

1. **Fixed Part**:
   - This part is independent of the size of the input and includes:
     - Constants: Space for constants used in the algorithm.
     - Simple variables: Space needed for variables, fixed-size variables, and program code.
   - This space is generally constant, \(O(1)\).

2. **Variable Part**:
   - This part depends on the size of the input and includes:
     - Dynamic memory allocation for arrays, lists, trees, etc.
     - Recursion stack space.
   - This part can grow as the size of the input increases.

## Total Space Complexity

The total space complexity of an algorithm can be represented as:
\[ \text{Total Space Complexity} = \text{Fixed Part} + \text{Variable Part} \]

## Examples of Space Complexity

1. **Constant Space Complexity** (\(O(1)\)):
   - Example: An algorithm that swaps two numbers uses a fixed amount of memory (two variables) regardless of the input size.
   ```python
   def swap(a, b):
       temp = a
       a = b
       b = temp
       return a, b
2.  **Linear Space Complexity** (O(n))

**Example:** An algorithm that creates a list of size \( n \) based on the input size.

```python
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
```


2.  **Quadratic Space Complexity** (O(n²))

**Example:** Example: An algorithm that creates a two-dimensional array (matrix) of size 

```python
def create_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    return matrix
```