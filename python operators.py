operators

"""
Comparision operators
=   Assignment 
==  Eqals 
!=  Not Equals
>   Greater than
<   less than
>=  Greater than or Equal to 
<=  less than or Eqals to
!>  Not Greater than
!<  Not less than

Arithmatic operators
+   Addition
-   Subtruction
/   Division
*   multiplication
//  Integer Division
**  Exponentiation
%   Modulus

Membership operators
is
Not
In


Logical oparetor
and
or
not

"""


a = 10
b = 3

# Addition
print(a + b)  # Output: 13

# Subtraction
print(a - b)  # Output: 7

# Multiplication
print(a * b)  # Output: 30

# Division
print(a / b)  # Output: 3.333...

# Floor Division
print(a // b)  # Output: 3

# Modulus
print(a % b)  # Output: 1

# Exponentiation
print(a ** b)  # Output: 1000


a = 10
b = 3

# Equal to
print(a == b)  # Output: False

# Not equal to
print(a != b)  # Output: True

# Greater than
print(a > b)  # Output: True

# Less than
print(a < b)  # Output: False

# Greater than or equal to
print(a >= b)  # Output: True

# Less than or equal to
print(a <= b)  # Output: False


a = True
b = False

# Logical AND
print(a and b)  # Output: False

# Logical OR
print(a or b)  # Output: True

# Logical NOT
print(not a)  # Output: False

a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND
print(a & b)  # Output: 0 (0000)

# Bitwise OR
print(a | b)  # Output: 14 (1110)

# Bitwise XOR
print(a ^ b)  # Output: 14 (1110)

# Bitwise NOT
print(~a)  # Output: -11 (inverts all bits)

# Bitwise Left Shift
print(a << 1)  # Output: 20 (10100)

# Bitwise Right Shift
print(a >> 1)  # Output: 5 (0101)


a = 10

# Assign
a = 5
print(a)  # Output: 5

# Add and assign
a += 3
print(a)  # Output: 8

# Subtract and assign
a -= 2
print(a)  # Output: 6

# Multiply and assign
a *= 4
print(a)  # Output: 24

# Divide and assign
a /= 3
print(a)  # Output: 8.0

# Floor divide and assign
a //= 2
print(a)  # Output: 4.0

# Modulus and assign
a %= 3
print(a)  # Output: 1.0

# Exponentiate and assign
a **= 2
print(a)  # Output: 1.0

# Bitwise AND and assign
a &= 1
print(a)  # Output: 1

# Bitwise OR and assign
a |= 2
print(a)  # Output: 3

# Bitwise XOR and assign
a ^= 1
print(a)  # Output: 2

# Bitwise left shift and assign
a <<= 1
print(a)  # Output: 4

# Bitwise right shift and assign
a >>= 1
print(a)  # Output: 2


a = 5
b = 5

# is operator
print(a is b)  # Output: True

# is not operator
print(a is not b)  # Output: False

# Different objects
c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)  # Output: False (different memory locations)
print(c == d)  # Output: True (same content)


x = 'hello'
y = {1, 2, 3, 'hello'}

# in operator
print('hello' in x)  # Output: True
print('hello' in y)  # Output: True

# not in operator
print('world' not in x)  # Output: True
print(4 not in y)  # Output: True




