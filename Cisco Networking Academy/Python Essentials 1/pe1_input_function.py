# Input function serve para usar INPUT do user or processos.

print("Tell me anything...")
anything = input("\n")
print("\nHmm...", anything, "... Really?")

# The input() function with an argument

something = input("Tell me anything...")
print("Hmm...", something, "...Really?")

# the input() function is invoked with one argument
#  ‒ it's a string containing a message;
# the message will be displayed on the console before
# the user is given an opportunity to enter anything;
# the result of the input() function is a string.


anything2 = input("\nEnter a number: ") # -> could have made type casting here as well.
something2 = int(anything2) ** 2.0 # We had to convert the anything variable in order for it to be an int
print(anything2, "to the power of 2 is", something2)

# Type casting (type conversions)

# int()
# float()
# str() - converts to string

leg_a = float(input("\nInput first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))


# -------------------------------------------------------------

# input a float value for variable a here
a = float(input("Give me the first number: "))
# input a float value for variable b here
b = float(input("Give me the second number: "))
# output the result of addition here
print("\nThis is the result of the addition:",a + b)
# output the result of subtraction here
print("This is the result of the subtraction:", a - b)
# output the result of multiplication here
print("This is the result of the multiplication:", a * b)
# output the result of division here
print("This is the result of the division:", a / b)

print("This is the result of a floor division :", a // b)

print("This is the result of the leftovers of the division:", a % b)

print("\nThat's all, folks!")