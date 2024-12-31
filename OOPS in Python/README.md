# Cluster Class in Python

This repository provides an introduction to creating a basic class in Python with attributes, methods, and the use of the `__init__` method and `self` keyword.

## Overview

In this example, we’ll create a `Cluster` class to represent a group of nodes in a cluster. This guide covers:
- Basics of creating a class
- Initializing attributes with `__init__`
- Using `self` to reference instance variables
- Creating methods for class functionality
- Example usage of the class

### 1\. Class Basics

A **class** is like a blueprint for creating objects. Each object has attributes (variables) and methods (functions) that define its behavior.

### 2\. Creating a Class

To create a class, use the `class` keyword followed by the class name (typically in PascalCase). Let's create a `Cluster` class, representing a group of nodes in a cluster.

```python
class Cluster:
    pass
```
This is an empty class. Let's add some attributes and methods to make it functional.

### 3\. Attributes of the Class and `__init__` Method

Attributes are variables that hold data about the class or object. The `__init__` method, known as the constructor, initializes the class attributes when an object is created.

The `self` keyword in Python is a reference to the current instance of the class. It allows you to access the instance's attributes and methods within the class.

Here's how to create attributes using `__init__`:

```python

`class Cluster:
    def __init__(self, name, nodes):
        # `name` and `nodes` are attributes of the class
        self.name = name  # name of the cluster
        self.nodes = nodes  # number of nodes in the cluster`
```

When we create an instance of `Cluster`, the `__init__` method is called automatically, and we can set `name` and `nodes` for each instance.

### 4\. Creating Methods in the Class

A method is a function defined within a class that performs operations using the object's data. Let's add a few methods to the `Cluster` class:

```python

class Cluster:
    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes

    # Method to display cluster details
    def display_info(self):
        print(f"Cluster Name: {self.name}")
        print(f"Number of Nodes: {self.nodes}")

    # Method to add more nodes to the cluster
    def add_nodes(self, count):
        self.nodes += count
        print(f"Added {count} nodes to the cluster.")
        print(f"Total nodes: {self.nodes}")`
```
### 5\. Creating an Object

Now that we have defined our class with attributes and methods, let's create an object (instance) of `Cluster`.

```python

# Creating an object of Cluster class
cluster1 = Cluster("DataCluster", 5)

# Accessing the object's attributes and methods
cluster1.display_info()  # Display initial info
cluster1.add_nodes(3)    # Add 3 more nodes`
```
### 6\. Explanation of `self` in Methods

-   **`self` as a reference**: Inside any method, the first parameter must be `self`, which refers to the instance of the class that is calling the method.
-   **Accessing Attributes and Methods**: Using `self.attribute_name` and `self.method_name()` allows us to access other attributes and methods within the class.

For example, in `display_info`, we use `self.name` and `self.nodes` to access the values stored in the instance that calls `display_info`.

### Full Example with Explanations

```python

class Cluster:
    # Initializing with name and number of nodes
    def __init__(self, name, nodes):
        self.name = name       # instance attribute for cluster name
        self.nodes = nodes     # instance attribute for number of nodes

    # Method to display cluster details
    def display_info(self):
        print(f"Cluster Name: {self.name}")
        print(f"Number of Nodes: {self.nodes}")

    # Method to add nodes to the cluster
    def add_nodes(self, count):
        self.nodes += count
        print(f"Added {count} nodes to the cluster.")
        print(f"Total nodes: {self.nodes}")

# Creating an instance (object) of the Cluster class
cluster1 = Cluster("DataCluster", 5)
cluster1.display_info()     # Output: Cluster Name: DataCluster, Number of Nodes: 5
cluster1.add_nodes(3)       # Output: Added 3 nodes, Total nodes: 8
```