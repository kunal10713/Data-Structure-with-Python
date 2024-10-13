# Python strings are immutable:

Python strings are immutable,  it means that the original string object itself cannot be modified. However, when you perform operations like concatenation (s + " World") or transformation (s.lower()), what actually happens is that a new string object is created rather than modifying the original one.

In your example:

```python
Copy code
s = "Hello"
s = s + " World"  # Creates a new string "Hello World"
print(s.lower())   # Output: "hello world"
```

Here’s what's happening behind the scenes:

1.  s = "Hello": A string object "Hello" is created, and s points to it.
2. s = s + " World": Python creates a new string object "Hello World" and assigns s to point to this new object. The original "Hello" string remains unchanged in memory (and will eventually be garbage collected).
3. s.lower(): This operation returns a new string "hello world" without modifying the original "Hello World" string. Again, the original string remains unchanged.

### Key Point:
- When you perform operations on strings, Python creates new string objects instead of modifying the original one. This is what makes Python strings immutable. Even though it looks like you're "changing" the string, you're really just creating new string objects and reassigning variables to them.


### Illustration:
1. Original String:

```python
s = "Hello"
```
s points to the string "Hello".

2. After Concatenation:

```python
s = s + " World"
```

Python creates a new string "Hello World" and s now points to this new string. The original "Hello" remains untouched.

3. After Transformation:

```python
s.lower()
```
This creates another new string "hello world" without changing the string "Hello World" that s currently references. If you don't assign the result to s, it won't change what `s` points to.

## Python's Immutability: 
- Immutability doesn't mean you `can't "change" what a variable refers to`, but rather that the underlying string objects cannot be altered once they are created.
