# As files get long, a way to keep them organized, we can store code in MODULES
# Modules are files consisting of Python code. They can define CLASSES, FUNCTIONS, VARIABLES, etc.

# Using modules facilitate simplicity, maintanability and reusability (DRY principle)

import random #this will search for the module so it allows us to use the code within it (reusability)

numbers = [1,2,3,4,5] # here we define a list containing the values within '[]' seperated by ','.


random.shuffle(numbers) # To use the function shuffle, 
                        # we write: module_name.function_name(variable) to be used here.
print(numbers)          # As we can see, it will shuffle the list elements everytime it is ran.


number = random.choice(numbers) # Trying another function of the random module, we now use the choice
print(number)                   # This will pick a number at random from the provided list.