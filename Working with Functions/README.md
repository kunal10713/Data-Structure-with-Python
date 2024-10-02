# Understanding Pass by Value in Python Functions

This document explains the concept of "pass by value" in Python, specifically in the context of variable and array updates. It also highlights the differences between Python's behavior and C++.

## 1. Overview of Pass by Value in Python

In Python, when you pass a variable (which can be either mutable or immutable) to a function and modify it, the outcome depends on the type of the object (mutable or immutable) and how you modify it. Let's break this down for both scenarios:



**Example:**

### 1. Variable Update in Python

**Immutable Objects (e.g., integers, strings, tuples)**
- If you pass an immutable object (like an integer or string) to a function and try to modify it, you will not change the original variable. Instead, you will create a new object in memory, and the original variable remains unchanged.


- When passing a variable to a function, if you reassign that variable inside the function, it does not affect the original variable outside the function. However, if you modify a mutable object, such as a list or a dictionary, the changes will reflect outside the function.

**Example:**

```python
def update_value(x):
    x = 10  # Reassigning x does not affect the original variable
    print("Inside function:", x)

value = 5
update_value(value)
print("Outside function:", value)
```

Output:
```
Inside function: 10
Outside function: 5
```

In this example, the original variable value remains unchanged because the reassignment of x does not affect the original reference.



### 2. Mutable Objects (e.g., lists, dictionaries)
If you pass a mutable object (like a list or dictionary) to a function and modify its contents (such as appending or changing an element), the original variable will be affected since both the parameter and the original variable reference the same object.



**Example:**

```python
def update_list(my_list):
    my_list.append(4)  # Modifies the original list
    print("Inside function:", my_list)

numbers = [1, 2, 3]
update_list(numbers)
print("Outside function:", numbers)
```

Output:
```
Inside function: [1, 2, 3, 4]
Outside function: [1, 2, 3, 4]
```

Here, appending to my_list affects numbers because they both refer to the same list object.

