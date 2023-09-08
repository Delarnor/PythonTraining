print(int(11_11_11) * int(2)) # Python allows long numbers to be seperated with _ for readability
                              # 111111 = 11_11_11 for python (3.6 onwards)
                              # -111111 = -11_11_11 negative numbers follow the same rule

# allows us to use numbers in an octal representation.
# If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.
# 0o123 is an octal number with a (decimal) value equal to 83.

print("\nThis",0O123,"equals in python as 0O123. It's an octal number.") # output = 83

# The second convention allows us to use hexadecimal numbers. 
# Such numbers should be preceded by the prefix 0x or 0X (zero-x).
# 0x123 is a hexadecimal number with a (decimal) value equal to 291.

print("\nThis number:",0X123,"is a hexadecimal number, written as 0X123.")

print()
# On the other hand, it's not only points that make a float. You can also use the letter e.
# When you want to use any numbers that are very large or very small, you can use scientific notation.
# Take, for example, the speed of light, expressed in meters per second. 
# Written directly it would look like this: 300000000

print(3E8) # The letter E (you can also use the lower-case letter e ‒
           # it comes from the word exponent) is a concise record of the phrase 
           # times ten to the power of.
           # Note:
                # the exponent (the value after the E) has to be an integer;
                # the base (the value in front of the E) may be either an integer or a float.
print()
# Python may sometimes choose different notation than you.

print(0.0000000000000000000001) # 1e-22 is the output.
# Python always chooses the more economical form of the number's presentation, 
# and you should take this into consideration when creating literals.
