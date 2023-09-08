# Iteration or "loops"
# Repeating the same action multiple times until it reaches a specified endpoint

# We need the data that is iterated
# We need to describe what happens with each iteration
# Indicate when the loop should stop

# Infinite loop is a bug that can occur when the ending condition is omitted or specified incorrectly

# In python we can create a loop using the FOR keyword

spices = [
    "salt",
    "pepper",
    "cumin",
    "turmeric"
]
# FOR statement lets us specify a VARIABLE that we can use in each iteration 
# of the loop to reference the current value.
# IN indicates that what follows if the SET of values that we want it iterate through.
for spice in spices: 
    print(spice)
print("No more boring omelettes!")

print("")
print("Part 2")
print("")

# WHILE statement is used to create a loop that checks if a condition is met. 
# It doens't rely on a collection of things to iterate through.

print("Count to 100 by fives: ")
i = 5
while i <= 100:
    print(i)
    i = i+5
    # same as i+=5
print("Operation complete.")