# Built-in Search Methods in Python Lists

In Python, arrays (or more commonly, lists) have built-in methods that can be used for searching. Here are a few methods that you can use to search for elements in a list:


### 1. `in` Keyword:
The simplest way to check if an element is present in a list is by using the in keyword. This performs a linear search operation, which means it checks each element in the list one by one. The time complexity for this operation is:

#### Time Complexity: O(n)

#### Example:
```python
my_list = [10, 20, 30, 40, 50]
if 30 in my_list:
    print("30 is present in the list.")
else:
    print("30 is not in the list.")
```

### 2. list.index(element):

The `index()` method returns the index of the first occurrence of the specified element. If the element is not found, it raises a `ValueError`. This method also performs a linear search, iterating through the list until it finds the element.

#### Time Complexity: O(n)

#### Example:
```python
my_list = [10, 20, 30, 40, 50]
index = my_list.index(30)  # Returns 2
print(f"Element 30 is at index {index}.")
```
#### Output:
```python
Element 30 is at index 2.
```