"""
python_numbers_complete_reference.py

PURPOSE:
This file explains almost every NUMBER-RELATED:
- data type
- operator
- built-in function
- standard library module
that Python provides.

RULE FOLLOWED:
👉 Every operation has an explanation COMMENT next to it
👉 Similar style to your original file
👉 Beginner → Advanced progression
"""

# ======================================================
# 1. BASIC NUMERIC DATA TYPES
# ======================================================

a = 10                  # int → whole number, unlimited precision
b = 10.5                # float → decimal number (IEEE 754, limited precision)
c = 2 + 3j              # complex → real + imaginary number

print(a, b, c)

# ======================================================
# 2. TYPE CHECKING FUNCTIONS
# ======================================================

print(type(a))          # type() → returns data type of variable
print(isinstance(a, int))   # isinstance() → checks type safely
print(isinstance(b, float))
print(isinstance(c, complex))

# ======================================================
# 3. ARITHMETIC OPERATORS
# ======================================================

x = 15
y = 4

print(x + y)            # + → addition
print(x - y)            # - → subtraction
print(x * y)            # * → multiplication
print(x / y)            # / → division (always float)
print(x // y)           # // → floor division (quotient only)
print(x % y)            # % → modulus (remainder)
print(x ** y)           # ** → exponentiation (power)

# ======================================================
# 4. ASSIGNMENT OPERATORS
# ======================================================

n = 10
n += 5                  # n = n + 5
n -= 2                  # n = n - 2
n *= 3                  # n = n * 3
n /= 2                  # n = n / 2
n //= 2                 # n = n // 2
n %= 3                  # n = n % 3
n **= 2                 # n = n ** 2

print(n)

# ======================================================
# 5. COMPARISON OPERATORS
# ======================================================

print(10 == 10)         # == equality
print(10 != 5)          # != not equal
print(10 > 5)           # > greater than
print(10 < 5)           # < less than
print(10 >= 10)         # >= greater or equal
print(10 <= 9)          # <= less or equal

# ======================================================
# 6. CHAINED COMPARISONS
# ======================================================

print(1 < 2 < 3)        # Python evaluates as: 1<2 AND 2<3
print(1 == 2 < 3)       # Evaluates as: (1==2) AND (2<3)

# ======================================================
# 7. BUILT-IN NUMERIC FUNCTIONS
# ======================================================

print(abs(-10))         # abs() → absolute value
print(round(12.5678))   # round() → rounds to nearest integer
print(round(12.5678, 2))# round(n, digits) → precision rounding
print(pow(2, 5))        # pow(x, y) → x**y
print(divmod(17, 5))    # divmod() → (quotient, remainder)
print(min(1, 5, 3))     # min() → smallest value
print(max(1, 5, 3))     # max() → largest value
print(sum([1, 2, 3]))   # sum() → sum of iterable

# ======================================================
# 8. INTEGER BASE CONVERSIONS
# ======================================================

print(bin(10))          # bin() → binary representation
print(oct(10))          # oct() → octal representation
print(hex(10))          # hex() → hexadecimal representation

print(int("1010", 2))   # int(str, base) → base-2 to decimal
print(int("12", 8))     # base-8 to decimal
print(int("A", 16))     # base-16 to decimal

# ======================================================
# 9. FLOAT REPRESENTATION & LIMITATIONS
# ======================================================

print(0.1 + 0.2)        # Floating-point precision issue
print(round(0.1 + 0.2, 2))  # Fix using rounding

# ======================================================
# 10. DECIMAL MODULE (HIGH PRECISION)
# ======================================================

from decimal import Decimal, getcontext

getcontext().prec = 28  # Set global decimal precision

d1 = Decimal("0.1")     # Decimal must be created from string
d2 = Decimal("0.2")

print(d1 + d2)          # Accurate decimal addition
print(d1 * d2)          # Accurate multiplication
print(d1 / d2)          # Accurate division

# ======================================================
# 11. FRACTIONS MODULE (RATIONAL NUMBERS)
# ======================================================

from fractions import Fraction

f1 = Fraction(2, 7)     # Exact fraction representation
f2 = Fraction(3, 7)

print(f1 + f2)          # Fraction addition
print(f1 - f2)          # Fraction subtraction
print(f1 * f2)          # Fraction multiplication
print(f1 / f2)          # Fraction division
print(f1.numerator)    # Numerator
print(f1.denominator)  # Denominator

# ======================================================
# 12. COMPLEX NUMBER OPERATIONS
# ======================================================

z1 = 2 + 3j
z2 = 4 + 5j

print(z1 + z2)          # Complex addition
print(z1 - z2)          # Complex subtraction
print(z1 * z2)          # Complex multiplication
print(z1 / z2)          # Complex division
print(z1.real)          # Real part
print(z1.imag)          # Imaginary part
print(abs(z1))          # Magnitude of complex number

# ======================================================
# 13. MATH MODULE (SCIENTIFIC FUNCTIONS)
# ======================================================

import math

print(math.sqrt(16))    # Square root
print(math.cbrt(27))    # Cube root
print(math.pow(2, 3))   # Power (float result)
print(math.floor(4.9))  # Floor
print(math.ceil(4.1))   # Ceil
print(math.trunc(4.9))  # Truncate decimal
print(math.factorial(5))# Factorial
print(math.gcd(12, 18)) # Greatest common divisor
print(math.lcm(4, 6))   # Least common multiple

# Trigonometry
print(math.sin(math.pi / 2))  # Sine
print(math.cos(0))            # Cosine
print(math.tan(0))            # Tangent

# Logarithms
print(math.log(10))           # Natural log
print(math.log10(100))        # Base-10 log
print(math.log2(8))           # Base-2 log

# Constants
print(math.pi)                # π
print(math.e)                 # Euler's number
print(math.inf)               # Infinity
print(math.nan)               # Not-a-number

# ======================================================
# 14. RANDOM MODULE
# ======================================================

import random

print(random.random())        # Random float [0.0, 1.0)
print(random.uniform(1, 5))  # Random float in range
print(random.randint(1, 10)) # Random integer (inclusive)
print(random.randrange(1, 10, 2)) # Random step-based integer

arr = [1, 2, 3, 4]
print(random.choice(arr))    # Random element
random.shuffle(arr)          # Shuffle list in-place
print(arr)

# ======================================================
# 15. BOOLEAN AS NUMBERS
# ======================================================

print(True + True)            # True = 1, False = 0
print(False * 10)

# ======================================================
# 16. BITWISE OPERATIONS
# ======================================================

p = 5     # 101
q = 3     # 011

print(p & q)                  # AND
print(p | q)                  # OR
print(p ^ q)                  # XOR
print(~p)                     # NOT
print(p << 1)                 # Left shift
print(p >> 1)                 # Right shift

# ======================================================
# 17. LARGE NUMBER SUPPORT
# ======================================================

print(2 ** 1000)              # Arbitrary precision integers

# ======================================================
# 18. STRING REPRESENTATION OF NUMBERS
# ======================================================

num = 22 / 7

print(str(num))               # User-friendly string
print(repr(num))              # Exact representation

# ======================================================
# END OF FILE
# ======================================================
