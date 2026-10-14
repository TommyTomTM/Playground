print("Hello, World")
print("Spam" * 5)

# Mathematical operators
3 + 2
2 * 10
4 // 2  #Integer Division
4.0 / 2
(9 + 8) * 32

1 != 2
1 < 2
2 > 3
1.0 >= 1
0.99 <= 1

# and combine them with logical operators
(1.0 <= 1) and (1.0 >= 1)
(2 < 1) or (2 > 1)
not (1 != 2)

# Variablen
pi = 3.1415926535897932
x = 90

# Convert degree to radiant
x_rad = x * (pi / 180)

# Convert it back to degree
x_new = x_rad * (180 / pi)

# Check if they are the same
x == x_new

# We can make the printed statement more elaborate
print("x =", x)
x = 45.0
print(f"x = {x}")
print(f"{x = }")

if x < 90:
    x = x * 2  # This section gets executed if the statement is true
else:
    x = x / 2  # And this if it is false

print(f"x = {x}")

if x < 45:
    x = x * 2
elif x < 90:
    x = x * 3  # If the first statement is false but the second true
else:
    x = x**2  # If none of the above statements is true
print(f"x = {x}")

# List of integers
[2, 4, 6, 8]
# List of strings
["A", "B", "C"]
# List of lists
[[2, 4, 6, 8], ["A", "B", "C"]]
# List of mixed types
[2, "A"]
# Assign a list to a variable
integers = [2, 4, 6, 8]
# Changing values
integers[1] = -4
# append something to a list
integers.append(10)
# combine to lists
integers + [1, 3]

# List of integers from 0 to 2
range(3)
# List of integers from 5 to 9
range(5, 10)
# List of integers from 10 to 1 in reverse order
range(10, 0, -1)

# For loops work best with lists or sets
sum = 0
for i in integers:
    sum = sum + i

mean = sum / len(integers)  # len computes the length of a list
print(mean)

# Find out how many even and how many odd number are in a list
odd = 0
even = 0
for i in range(1, 10):
    if i % 2:
        odd = odd + 1
    else:
        even = even + 1

print(f"{even = }, {odd = }")

# While loops run until a statement is no longer true
a = 5
b = 2
c = 1
while a > 0:
    a = a - 1
    c = c * b
print(f"{b}^5 = {c}")


import math

mean = math.fsum(integers) / len(integers)
print(mean)

c = math.pow(2, 6)
print(c)

# Just testing