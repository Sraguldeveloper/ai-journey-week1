# Python Complete Cheat Sheet

## Variables and Data Types

### Creating Variables
```python
x = 5
y = 3.14
z = "Hello"
```

### Basic Data Types
- **Text Type:** `str`
- **Numeric Types:** `int`, `float`, `complex`
- **Sequence Types:** `list`, `tuple`, `range`
- **Mapping Type:** `dict`
- **Set Types:** `set`, `frozenset`
- **Boolean Type:** `bool`
- **Binary Types:** `bytes`, `bytearray`, `memoryview`
- **None Type:** `NoneType`

### Checking Variable Type
```python
type(x)  # Returns the data type
```

### Dynamic Typing
```python
x = 10        # int
x = "string"  # str - same variable can hold different types
```

### Type Hints
```python
variable: data_type = value
age: int = 25
```

---

## Operators

### Arithmetic Operators
| Operator | Name | Example |
|----------|------|---------|
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| // | Floor Division | x // y |
| % | Modulus | x % y |
| ** | Exponentiation | x ** y |

### Assignment Operators
| Operator | Example |
|----------|---------|
| = | x = 5 |
| += | x += 3 |
| -= | x -= 3 |
| *= | x *= 3 |
| /= | x /= 3 |
| //= | x //= 3 |
| %= | x %= 3 |
| **= | x **= 3 |

### Comparison Operators
| Operator | Name | Example |
|----------|------|---------|
| == | Equal | x == y |
| != | Not equal | x != y |
| > | Greater than | x > y |
| < | Less than | x < y |
| >= | Greater than or equal | x >= y |
| <= | Less than or equal | x <= y |

### Logical Operators
| Operator | Description | Example |
|----------|-------------|---------|
| and | Returns True if both statements are true | x > 5 and x < 10 |
| or | Returns True if one of the statements is true | x > 5 or x < 4 |
| not | Reverses the result | not(x > 5) |

### Membership Operators
| Operator | Description | Example |
|----------|-------------|---------|
| in | Returns True if a sequence contains the specified value | x in list |
| not in | Returns True if a sequence does not contain the specified value | x not in list |

---

## Strings

### Creating Strings
```python
a = "Hello"
a = 'Hello'
a = """Multi-line
string"""
```

### String as Array
```python
a = "Hello, World!"
print(a[1])        # Output: 'e' (index starts at 0)
print(a[-1])       # Output: '!'
print(a[2:5])      # Output: 'llo' (slicing)
```

### String Length
```python
len(a)  # Returns length
```

### String Methods
| Method | Description |
|--------|-------------|
| upper() | Converts string to uppercase |
| lower() | Converts string to lowercase |
| strip() | Removes whitespace from ends |
| replace() | Replaces substring |
| split() | Splits into list |
| join() | Joins list into string |
| find() | Searches for substring |
| startswith() | Checks if starts with substring |
| endswith() | Checks if ends with substring |
| isdigit() | Checks if all characters are digits |
| isalpha() | Checks if all characters are alphabetic |

### String Operations
```python
# Check if character/phrase exists
if "free" in txt:
    print("Yes")

if "expensive" not in txt:
    print("Not present")
```

### String Concatenation
```python
x = "Hello"
y = "World"
z = x + " " + y
```

---

## Lists

### Creating Lists
```python
mylist = ["apple", "banana", "cherry"]
mylist = list((1, 2, 3))  # Using constructor
```

### List Characteristics
- **Ordered:** Items have defined order
- **Changeable:** Can modify items
- **Allow Duplicates:** Can have same values multiple times

### Accessing List Items
```python
print(mylist[0])      # First item
print(mylist[-1])     # Last item
print(mylist[1:3])    # Slicing
```

### Modifying Lists
```python
mylist[0] = "orange"         # Change item
mylist.append("orange")      # Add item at end
mylist.insert(1, "orange")   # Insert at specific position
mylist.extend(["grape"])     # Add multiple items
mylist.remove("banana")      # Remove specific item
mylist.pop(0)                # Remove by index
mylist.pop()                 # Remove last item
del mylist[0]                # Delete by index
mylist.clear()               # Remove all items
```

### List Methods
| Method | Description |
|--------|-------------|
| append() | Adds item at end |
| insert() | Adds item at specific position |
| remove() | Removes first occurrence |
| pop() | Removes item at index |
| clear() | Removes all items |
| index() | Returns index of first occurrence |
| count() | Returns count of specified item |
| sort() | Sorts list |
| reverse() | Reverses order |
| copy() | Returns shallow copy |

### List Length
```python
len(mylist)
```

### Looping Through Lists
```python
for item in mylist:
    print(item)
```

---

## Tuples

### Creating Tuples
```python
mytuple = ("apple", "banana", "cherry")
mytuple = tuple(("apple", "banana"))  # Using constructor
```

### Tuple Characteristics
- **Ordered:** Items have defined order
- **Unchangeable:** Cannot modify items
- **Allow Duplicates:** Can have same values

### Accessing Tuple Items
```python
print(mytuple[0])     # First item
print(mytuple[-1])    # Last item
print(mytuple[1:3])   # Slicing
```

### Single Item Tuple
```python
thistuple = ("apple",)  # Note the comma!
# Without comma, Python doesn't recognize it as tuple
```

### Tuple Length
```python
len(mytuple)
```

---

## Dictionaries

### Creating Dictionaries
```python
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict = dict(name="John", age=36)  # Using constructor
```

### Dictionary Characteristics
- **Ordered:** Items have defined order (Python 3.7+)
- **Changeable:** Can modify items
- **No Duplicates:** Cannot have duplicate keys

### Accessing Dictionary Items
```python
print(thisdict["brand"])           # By key
print(thisdict.get("brand"))       # Using get()
print(thisdict.keys())             # All keys
print(thisdict.values())           # All values
print(thisdict.items())            # Key-value pairs
```

### Modifying Dictionaries
```python
thisdict["year"] = 2020            # Change value
thisdict["color"] = "red"          # Add new item
thisdict.update({"year": 2020})    # Update multiple
del thisdict["year"]               # Delete item
thisdict.pop("year")               # Remove by key
thisdict.popitem()                 # Remove last item
thisdict.clear()                   # Remove all items
```

### Dictionary Methods
| Method | Description |
|--------|-------------|
| get() | Returns value for key |
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| update() | Updates dictionary |
| pop() | Removes by key |
| popitem() | Removes last item |
| clear() | Removes all items |
| copy() | Returns shallow copy |

### Dictionary Length
```python
len(thisdict)
```

### Looping Through Dictionary
```python
for key in thisdict:
    print(key)

for value in thisdict.values():
    print(value)

for key, value in thisdict.items():
    print(key, value)
```

---

## Sets

### Creating Sets
```python
myset = {"apple", "banana", "cherry"}
myset = set(("apple", "banana"))  # Using constructor
```

### Set Characteristics
- **Unordered:** Items have no defined order
- **Unchangeable:** Items cannot be changed (but can add/remove)
- **No Duplicates:** Cannot have duplicate values
- **No Indexing:** Cannot access by index

### Adding to Sets
```python
myset.add("orange")              # Add single item
myset.update(["grape", "mango"]) # Add multiple items
```

### Removing from Sets
```python
myset.remove("banana")      # Removes, raises error if not found
myset.discard("banana")     # Removes, no error if not found
myset.pop()                 # Removes random item
myset.clear()               # Removes all items
```

### Set Methods
| Method | Description |
|--------|-------------|
| add() | Adds item |
| update() | Adds multiple items |
| remove() | Removes item (error if not found) |
| discard() | Removes item (no error) |
| pop() | Removes random item |
| clear() | Removes all items |
| union() | Returns union of sets |
| intersection() | Returns intersection |
| difference() | Returns difference |

### Set Length
```python
len(myset)
```

---

## Conditional Statements

### If Statement
```python
if x > 5:
    print("x is greater than 5")
```

### If-Else Statement
```python
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

### If-Elif-Else Statement
```python
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

### Short Hand If
```python
if a > b: print("a is greater than b")
```

### Short Hand If-Else
```python
print("A") if a > b else print("B")
```

### Multiple Conditions
```python
if x > 5 and y < 10:
    print("Both conditions are true")

if x > 5 or y < 10:
    print("At least one condition is true")
```

---

## Loops

### For Loop
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

### Looping Through String
```python
for x in "banana":
    print(x)
```

### Break Statement
```python
for x in fruits:
    if x == "banana":
        break
    print(x)
```

### Continue Statement
```python
for x in fruits:
    if x == "banana":
        continue
    print(x)
```

### Range Function
```python
for x in range(6):           # 0 to 5
    print(x)

for x in range(2, 6):        # 2 to 5
    print(x)

for x in range(2, 30, 3):    # Start, stop, step
    print(x)
```

### Else in For Loop
```python
for x in range(6):
    print(x)
else:
    print("Finally finished!")
```

### Nested Loops
```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
```

### While Loop
```python
i = 1
while i < 6:
    print(i)
    i += 1
```

### While with Break
```python
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
```

### While with Continue
```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
```

### While-Else
```python
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
```

### Pass Statement
```python
for x in [0, 1, 2]:
    pass  # Loop cannot be empty
```

---

## Functions

### Creating Functions
```python
def my_function():
    print("Hello from a function")

# Call function
my_function()
```

### Function with Parameters
```python
def my_function(name):
    print("Hello, " + name)

my_function("John")
```

### Function with Return Value
```python
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)
```

### Default Parameter Value
```python
def my_function(country="Norway"):
    print("I am from " + country)

my_function()
my_function("Sweden")
```

### Passing Arguments as Dictionary
```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### Passing List as Argument
```python
def my_function(*args):
    for arg in args:
        print(arg)
```

### Function Naming Rules
- Must start with letter or underscore
- Can only contain letters, numbers, underscores
- Case-sensitive

### Pass Statement in Function
```python
def my_function():
    pass  # Function cannot be empty
```

---

## Classes and Objects

### Creating a Class
```python
class MyClass:
    x = 5
```

### Creating an Object
```python
p1 = MyClass()
print(p1.x)
```

### The __init__() Function
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
```

### Object Methods
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```

### Deleting Objects
```python
del p1
```

### Pass Statement
```python
class Person:
    pass  # Class cannot be empty
```

---

## Inheritance

### Parent Class
```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
```

### Child Class
```python
class Student(Person):
    pass
```

### Using super()
```python
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
```

### Adding Properties to Child Class
```python
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
```

### Adding Methods to Child Class
```python
class Student(Person):
    def welcome(self):
        print(f"Welcome {self.firstname} to class of {self.graduationyear}")
```

### Method Overriding
```python
class Student(Person):
    def printname(self):
        print("Student:", self.firstname, self.lastname)
```

---

## Modules

### Creating a Module
```python
# Save in mymodule.py
def greeting(name):
    print("Hello, " + name)

person1 = {"name": "John", "age": 36}
```

### Using a Module
```python
import mymodule
mymodule.greeting("Jonathan")
a = mymodule.person1["age"]
print(a)
```

### Renaming a Module
```python
import mymodule as mx
a = mx.person1["age"]
```

### Importing Specific Items
```python
from mymodule import person1
print(person1["age"])
```

### dir() Function
```python
import platform
x = dir(platform)
print(x)
```

### Built-in Modules
```python
import platform
x = platform.system()
print(x)
```

---

## Exception Handling

### Try-Except
```python
try:
    print(x)
except:
    print("An exception occurred")
```

### Multiple Exceptions
```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
```

### Else Block
```python
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
```

### Finally Block
```python
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
```

### Raising Exceptions
```python
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
```

---

## Built-in Functions

| Function | Description |
|----------|-------------|
| len() | Returns length |
| type() | Returns data type |
| str() | Converts to string |
| int() | Converts to integer |
| float() | Converts to float |
| list() | Creates list |
| tuple() | Creates tuple |
| dict() | Creates dictionary |
| set() | Creates set |
| print() | Prints output |
| input() | Gets user input |
| range() | Returns sequence |
| sum() | Returns sum of items |
| min() | Returns minimum value |
| max() | Returns maximum value |
| sorted() | Returns sorted list |
| reversed() | Returns reversed list |
| abs() | Returns absolute value |
| round() | Rounds number |
| pow() | Returns power |
| divmod() | Returns quotient and remainder |
| enumerate() | Returns enumerated list |
| zip() | Zips iterables |
| map() | Maps function to items |
| filter() | Filters items |
| all() | Returns True if all items true |
| any() | Returns True if any item true |
| dir() | Lists attributes |
| id() | Returns unique id |
| isinstance() | Checks instance type |
| issubclass() | Checks subclass |
| hasattr() | Checks if attribute exists |
| getattr() | Gets attribute value |
| setattr() | Sets attribute value |
| delattr() | Deletes attribute |

---

## File Handling

### Opening Files
```python
f = open("demofile.txt")
f = open("demofile.txt", "r")  # Read (default)
f = open("demofile.txt", "w")  # Write
f = open("demofile.txt", "a")  # Append
f = open("demofile.txt", "x")  # Create
```

### Reading Files
```python
f = open("demofile.txt", "r")
print(f.read())        # Read entire file
print(f.readline())    # Read one line
f.close()
```

### Writing to Files
```python
f = open("demofile.txt", "w")
f.write("Hello")       # Write to file
f.close()
```

### Creating Files
```python
f = open("myfile.txt", "x")  # Create new file
f.close()
```

### Deleting Files
```python
import os
os.remove("myfile.txt")
```

---

## Quick Reference

### Python Version
```python
import sys
print(sys.version)
```

### Print Multiple Values
```python
print("Value 1:", x, "Value 2:", y)
```

### Comments
```python
# Single line comment
''' 
Multi-line comment
'''
```

### Variable Naming Rules
- Must start with letter or underscore
- Can contain letters, numbers, underscores
- Case-sensitive
- Use snake_case convention

### Best Practices
- Use descriptive variable names
- Write comments for complex code
- Follow PEP 8 style guide
- Use meaningful function names
- Keep functions small and focused
