# Basic Operators

# Exponentiation
    # when both ** arguments are integers, the result is an integer, too;
    # when at least one ** argument is a float, the result is a float, too.
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print ("\nMultiplication") # Multiplication

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print("\nDivision") # Division

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# The result produced by the division operator is always a float, regardless of whether
# or not the result seems to be a float at first glance: 1 / 2,
# or if it looks like a pure integer: 2 / 1.

print("\nFloor division") # its result lacks the fractional part ‒ it's absent (for integers), 
                          # or is always equal to zero (for floats); 
                          # this means that the results are always rounded;
                          # it conforms to the integer vs. float rule.
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print("\n Remainder") # Remainder (modulo)

# The result of the operator is a remainder left after the integer division.
print(14 % 4) # output is 2


# Operators and their bindings

# The binding of the operator determines the order of computations
# performed by some operators with equal priority, put side by side in one expression.

print(9 % 6 % 2) # left side binding, output = 1

# Repeat the experiment, but now with exponentiation.

print(2 ** 2 ** 3) # right side binding, output = 256
# the 2 ** 3 is calculated first (2x2x2=8) and then the 2 ** 8 is calculated (2x2x2x2x2x2x2x2 = 256)

print()
print(2 * 3 % 5)

# A unary operator is an operator with only one operand, e.g., -1, or +3.
# A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.