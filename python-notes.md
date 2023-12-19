programming: i/o & processing

### frontend
javascript typescript npm yarn webpack parcel
design systems component libraries
common npm packages

### middleware/backend
docker kubernetes linux devops CI/CD jenkins github webhooks python

Random questions: I wonder: do most large companies' IT/devops use scripting to bundle npm dependencies? and maybe mid-sized companies use scripting to configure a bundler like webpack? and then startups work with pre-built template apps? It's pretty daunting to think about the number of libraries/packages that needs to be run in a browser or mobile browser to make an app work and I'm so excited to see how script-writers (?) accomplish it and work around migrations and evolving code.

6/26 - notes

fundamentals of programming concepts including data types, variables, decision statements, loops, functions and file handling

i/o (file handling using all the rest)

processing (not as much file handling)

common scripting language constructs: lists, literals, regular expressions

incrementally evolving ai from python to other languages 

variables/literals - integers, floats and strings

This package will install Python 3.11.4 for macOS 10.9 or later for the following architecture(s): arm64, x86_64.

Reserved keywords python

False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield

{:.2f} two decimal place formatting

x % 10000 yield last four digits

script is a file; can be input to the interpreter
module: a file imported by a script, module or interpreter
math module: theoretic, trigonometric, and logarithmic operations

unicode representation = "code point" (over 1m code points which each have a decimal encoding) (ord() and chr())

r = raw string
, end='' = no newline
, sep='' = no spaces btw args
, flush=True = can help with buffer errors

https://docs.python.org/3.7/howto/unicode.html

lists, tuples, and dictionaries

"Data types: String basics, list basics, dictionary basics, types summary, additional practice, type conversions

Strings: String formatting, advanced string formatting, string slicing, string methods, string split and join"

default_is_string = input('optional prompt')

len()

strings: immutable; must use assignment to update entire string

list.append(value)
list.pop(i)
list.remove(value)

dict: key is immutable type (e.g.: number, string, tuple) and value is any type

KeyError

containers:
mapping types (dict) and sequence types: string, list (mutable), tuple ((use len() and []))

relational operators (<, <=, >, >=), equality operators (==, !=), membership operators (in, not in), and identity operators (is, is not)

"Good practice is to always use the equality operator== when comparing values."

input_string = input().strip().lower().slice() 
parse input tokens

https://www.jetbrains.com/help/pycharm/

ML neural networks math: vector, scalar, matmul, tensor
https://numpy.org/

"Vectors and Matrices
The two primary mathematical entities that are of interest in linear algebra are the vector and the matrix. They are examples of a more general entity known as a tensor. Tensors possess an order (or rank), which determines the number of dimensions in an array required to represent it."
[source](https://www.quantstart.com/articles/scalars-vectors-matrices-and-tensors-linear-algebra-for-deep-learning-part-1/#:~:text=Vectors%20and%20Matrices,array%20required%20to%20represent%20it.)

floats: don't use == due to imprecision

ternary operator (conditional expressions): ideal for assignment statement such as:

y = 1 if x==2 else x * 2

edge-cases and corner-cases
input parsing and checking

while input_string.isdigit():
reversed()

"While loops are commonly used for counting a specific number of iterations, and for loops are commonly used to iterate over all elements of a container. The range() function allows counting in for loops as well."

"A for loop combined with range() is generally preferred over while loops, since for loops are less likely to become stuck in an infinite loop situation."

"Use a for loop when the number of iterations is computable before entering the loop, as when counting down from X to 0, printing a string N times, etc.
Use a for loop when accessing the elements of a container, as when adding 1 to every element in a list, or printing the key of every entry in a dict, etc.
Use a while loop when the number of iterations is not computable before entering the loop, as when iterating until a user enters a particular character."

loops:

```py
for i in range(num_rows):
    for j in range(num_cols):
```

```py
num_rows = int(input())
num_cols = int(input())

seat_num = 1
seat_char = 'A'

for i in range(num_rows):
    for j in range(num_cols):
        print('{}{}'.format(seat_num, seat_char), end=' ')
        seat_char = chr(ord(seat_char) + 1)
    seat_num += 1
    seat_char = 'A'
    
print()
```

continue and break:
```py
for i in range(10):
    if pattern1[i] == pattern2[i]:
        score += 1
        continue
    else:
        break
```

enumerate() example:

```py
origins = [4, 8, 10]

for (index, value) in enumerate(origins):
    print('Element {}: {}'.format(index, value))
```

word = input()
password = ''

''' Type your code here. Myp@ssw.rdq*s'''

for i in range(len(word)):
    pass_char = word[i]
    print(pass_char)
    
```py
import random

seedVal = int(input("What seed should be used? "))
random.seed(seedVal)
print('')

lower = int(input("What is the lower bound?\n"))
upper = int(input("What is the upper bound?\n"))

while upper <= lower:
    print('Lower bound must be less than upper bound.')
    lower = int(input("What is the lower bound?\n"))
    upper = int(input("What is the upper bound?\n"))
    
answer = random.randint(lower, upper)
guess = int(input('What is your guess?\n'))
while (guess != answer):
    if (guess > answer):
        print('Nope, too high.')
    else: 
        print('Nope, too low.')
    guess = int(input('What is your guess?\n'))
print('You got it!')
```

"A variable must be marked as global only if the function needs to write that variable. Reading a global variable does not require a global statement."

A programmer can examine the names in the current local and global namespace by using the locals() and globals() built-in functions."

"If the object is immutable, such as a string or integer, then the modification is limited to inside the function. Any modification to an immutable object results in the creation of a new object in the function's local scope, thus leaving the original argument object unchanged.

If the object is mutable, then in-place modification of the object can be seen outside the scope of the function. Any operation like adding elements to a container or sorting a list that is performed within a function will also affect any other variables in the program that reference the same object."

"pass a copy of the object as the argument instead, like in the statement `my_func(my_list[:])`." //  use slice notation with no start or end indices

"A common error is to provide a mutable object, like a list, as a default parameter. Such a definition can be problematic because the default argument object is created only once, at the time the function is defined (when the script is loaded), and not every time the function is called. Modification of the default parameter object will persist across function calls, which is likely not what a programmer intended. The below program demonstrates the problem with mutable default objects and illustrates a solution that creates a new empty list each time the function is called."

"`if my_list == None:`  # Create a new list if a list was not provided"

"`del` performs in-place modification, returning the same list without the deleted element.

List concatenation appends the right operand to the left operand and creates a new list with the result."

```py
for my_var in my_list:
    # Loop body statements go here

for index in range(len(nums)):
    value = nums[index]
    print('{}: {}'.format(index, value))
```
```py
currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
   for column_index, item in enumerate(row):
       print('currency[{}][{}] is {:.2f}'.format(row_index, column_index, item))

for pos, val in enumerate(nums):  
    print('{}: {}'.format(pos, val))

for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()
```
```py
user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
mult_table = [[int(num) for num in line.split()] for line in lines]
```
new_list = [expression for name in iterable]

more-efficient execution by the interpreter

"The contents of this command line are automatically stored in the list sys.argv, which is stored in the standard library sys module. sys.argv consists of one string element for each argument typed on the command line."

`python myprog.py Name 30`

```py
import sys

if len(sys.argv) != 3:
    print('Usage: python myprog.py name age\n')
    sys.exit(1)  # Exit the program, indicating an error with 1.

name = sys.argv[1]
age = int(sys.argv[2])

print('Hello {}. '.format(name))
print('{} is a great age.\n'.format(age))
```

```py
m1_rows = 4
m1_cols = 2
m2_rows = m1_cols  # Must have same value
m2_cols = 3

m1 = [
    [3, 4],
    [2, 3],
    [1, 2],
    [0, 2]
]

m2 = [
    [5, 4, 4],
    [0, 2, 3]
]

m3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# m1 * m2 = m3
for i in range(m1_rows):  # for each row of m1
    for j in range(m2_cols):  # for each column of m2
        # Compute dot product
        dot_product = 0
        for k in range(m2_rows): #  for each row of m2
            dot_product += m1[i][k] * m2[k][j]

        m3[i][j] = dot_product

for i in range(m1_rows):
    for j in range(m2_cols):
        print('{}'.format(m3[i][j]), end=' ')
    print()  # Print single newline

```

nested dictionary:
`{'D1': {'D2': 'x'}}`


```py
user_input = input()
entries = user_input.split('   ')
replacement_pairs = {}

for pair in entries:
    split_pair = pair.split(' ')
    replacement_pairs[split_pair[0]] = split_pair[1]
    # replacement_pairs is a dictionary
```

reading files
```py
def read_file(filename):
     input_file = open(filename, “r”)
     file_contents = []
     for line in input_file:
          file_contents.append(line)
     close(filename)
     return file_contents
```

#tolearn:
- `Shadows name '' from outer scope` 
- best practices for global variables
- namespaces
- scope
- passing variable names to functions


```py
import os

os.stat('file.txt')
os.remove('file.txt')

# in stdlib
open()
file.close()
my_file.readlines() 
f.write()

# Force output buffer to be written to disk
f.flush()
os.fsync(f.fileno())

"""Echo the contents of a file."""
f = open('myfile.txt')

for line in f:
    print(line, end="")

f.close()

# path portability across systems
path = os.path.join('subdir', 'file.ext')
# stores file separator across systems
.split(os.path.sep) 
os.path.exists(path)
os.path.isfile(path)
os.path.getsize(path)
os.walk()

bytes()

# creates a sequence of bytes by encoding the string using ASCII.
bytes('A text string', 'ascii')

# creates a sequence of 100 bytes whose values are all 0.
bytes(100) 

# creates a sequence of 3 bytes with values from the list.
bytes([12, 15, 20]) 

print(b'123456789 is the same as \x31\x32\x33\x34\x35\x36\x37\x38\x39')
# output: b'123456789 is the same as 123456789'

# Assign x to a bytes object with a single byte whose hexadecimal value is 0x1a. Use a bytes literal.
x = b'\x1a'

# Assign x to a bytes object containing three bytes with hexadecimal values 0x05, 0x15, and 0xf2. Use a bytes literal.
x = b'\x05\x15\xf2'

# module for packing values into sequences of bytes and unpacking sequences of bytes into values (like integers and strings)
import struct

# Converts byte sequence into integer object
pixel_data_loc = struct.unpack('<L', pixel_data_loc)[0]


import sys

sys.argv
sys.exit

# context manager
# the file object returned by open() is bound to myfile. When the statements in the block complete, then myfile is closed. 
with open('myfile.txt', 'r') as myfile:
    # Statement-1
    # Statement-2
    # ...
    # Statement-N
```

writing and reading files lab
switching back and forth btw dicts and lists
```py
file = input()
f = open(file)
arr = f.readlines()
count = 0
dict = {}

while count != len(arr):
    value = ''
    key = int(arr[count])
    count += 1
    if key not in dict:
        value = str(arr[count]).split('\n')[0]
    else:
        new_val = dict[key] + '; ' + str(arr[count]).split('\n')[0]
        value = new_val
    count += 1
    dict[key] = value

sorted_keys = sorted(dict)
sorted_dict = {}
unsorted_titles = []

for key in sorted_keys:
    sorted_dict[key] = dict[key]
    
f1 = open('output_keys.txt', 'w')
f2 = open('output_titles.txt', 'w')

for i in sorted_dict:
    line = '{}: {}\n'.format(i, sorted_dict[i])
    f1.write(line)
    
    title = sorted_dict[i]
    if ';' in title:
        titles = title.split('; ')
        for i in range(len(titles)):
            indiv_title = titles[i]
            if i < len(titles):
                unsorted_titles.append(indiv_title)
            else:
                title_tokens = indiv_title.split('\n')
                unsorted_titles(title_tokens[0])
    else:
        unsorted_titles.append(title)

unsorted_titles.sort()

for title in unsorted_titles:
    f2.write(title + '\n')

f1.close()
f2.close()
```

special methods: double underscores
`self` - first parameter of a class method

"Class and instance objects are namespaces used to group data and functions together. A class attribute is shared amongst all of the instances of that class. Class attributes are defined within the scope of a class."

class attribute - kinda like a global for all the instances of the class; makes sense if it's a const

instance attribute - unique to the instance 

"If a name is not found in an instance namespace, then the class namespace is searched."

"A class interface consists of the methods that a programmer calls to create, modify, or access a class instance."

"Good practice is to prepend an underscore to methods only used internally by a class."

"A class interface should be the only necessary way to interact with a class instance."

decorator pattern: decorate object 
"used to modify the functionality of an object at runtime. At the same time other instances of the same class will not be affected by this, so individual object gets the modified behavior."

leetcode

neetcode 1 easy

```py
class DynamicArray(type_str: str, capacity: int, *args):
    arguments = args
    type_array = type_str
    capacity = capacity 
    
    def __init__(self, capacity: int, arguments):
        if capacity < 0:
            print('invalid capacity')
            break
        else:
            dynamic_array = [capacity]
        if ("getSize" in args):
            getSize()    
        if ("getCapacity" in args):
            getCapacity()
        if ("pushback" in args):
            i = index("pushback")
            pushback(i + 1)

    def get(self, i: int) -> int:
        return dynamic_array[i]

    def insert(self, i: int, n: int) -> None:
        insert(i, n)

    def pushback(self, n: int) -> None:
        append(n)

    def popback(self) -> int:
        return pop()

    def resize(self) -> None:
        dynamic_array = [length(dynamic_array) * 2]

    def getSize(self) -> int:
        return length(dynamic_array) - 1
    
    def getCapacity(self) -> int:
        return capacity
```