# Imagine that your computer program loves Spathiphyllum. 
# Whenever it receives an input in the form of the word Spathiphyllum,
# it involuntarily shouts to the console the following
# string: "Spathiphyllum is the best plant ever!"

# Write a program that utilizes the concept of conditional execution,
# takes a string as input, and:

# prints the sentence "Yes - Spathiphyllum is the best plant ever!" 
# to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" 
# if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" 
# otherwise. Note: [input] is the string taken as input.

answer = input("Can you guess my favourite plant? ")

if answer == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif answer == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not",answer,"!")