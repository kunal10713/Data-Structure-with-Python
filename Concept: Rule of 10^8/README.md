# Understanding the 10^8 Rule for Time Complexity

## What is the "10^8 Rule"?

When solving competitive programming or algorithmic problems, a crucial consideration is ensuring that your solution runs within a reasonable amount of time. The "10^8 rule" is a heuristic that helps estimate whether an algorithm will run efficiently given typical constraints.

### The Rule Explained
- Most programming competitions and coding platforms allow a maximum execution time of **1-2 seconds** for each problem.
- Modern processors can typically perform around **100 million (10^8) basic operations** in **1 second**.
- Therefore, **if your algorithm performs at most 10^8 operations**, it will likely run within 1 second and be accepted as an efficient solution.

### Why 10^8?
The number 10^8 is a rough estimate of how many operations a modern CPU can handle in 1 second. This estimate is based on:
- Processor speed
- Instruction cycles
- The type of operations performed

While the actual number of operations can vary depending on the complexity of individual instructions and specific hardware, 10^8 is used as a general rule of thumb to keep things simple.

## Applying the Rule in Problem Solving

The "10^8 rule" helps you quickly estimate the feasibility of your algorithm by considering its time complexity and the size of input data. Below are examples to see how it works:

### Example 1: Constant Time Complexity (O(1))
If an algorithm has **O(1)** complexity, it performs a fixed number of operations regardless of input size. It will execute within 1 second even for very large inputs, so it will always be efficient.

### Example 2: Linear Time Complexity (O(n))
- Consider an algorithm with **O(n)** complexity.
- If `n` is the size of the input, we need to ensure that `n` is less than or equal to **10^8** for it to run within 1 second.
  - For `n = 10^7`, it should run in less than 1 second.
  - For `n = 10^9`, it would exceed the limit and likely run out of time.

### Example 3: Quadratic Time Complexity (O(n^2))
- Suppose we have an algorithm with **O(n^2)** complexity.
- To find the largest possible `n` that runs efficiently:
  - Solve `n^2 <= 10^8` → `n <= sqrt(10^8)` → `n <= 10^4`.
- Thus, for quadratic algorithms, if `n` is larger than 10^4 (10,000), it may exceed the time limit.

### Example 4: Logarithmic Time Complexity (O(log n))
- For `n = 10^8`, the number of operations is:
  - `log2(10^8) ≈ 27` operations.(since 2^27 ≈ 10^8)
- This is highly efficient, running in less than 1 second for even large input sizes.

### Example 5: O(n log n) Complexity
- Suppose the algorithm is **O(n log n)**.
- For `n = 10^6`, the number of operations is:
  - `10^6 * log2(10^6) ≈ 10^6 * 20 = 2 * 10^7`.
- This is well within the limit of 10^8, so it should run efficiently for input sizes up to 1,000,000.

### Applying the Rule
To estimate whether an algorithm is feasible:
1. **Determine the time complexity** of your algorithm (e.g., O(n), O(n^2)).
2. **Estimate the maximum number of operations** based on input size and complexity.
3. **Compare against 10^8 operations** to see if it’s within 1 second.

## Quick Reference for Time Complexities and Input Limits

| Time Complexity | Maximum Input Size (`n`) for 1 Second |
|-----------------|---------------------------------------|
| O(1)            | Any size (`n`)                        |
| O(log n)        | `n` ≤ 10^18                           |
| O(n)            | `n` ≤ 10^8                            |
| O(n log n)      | `n` ≤ 10^6                            |
| O(n^2)          | `n` ≤ 10^4                            |
| O(n^3)          | `n` ≤ 500                             |
| O(2^n)          | `n` ≤ 20                              |
| O(n!)           | `n` ≤ 10                              |

## Conclusion
The "10^8 rule" is a helpful guideline for estimating whether your algorithm will run efficiently given typical constraints in competitive programming. By understanding time complexity and using this rule, you can quickly determine whether your solution needs optimization before submission.
