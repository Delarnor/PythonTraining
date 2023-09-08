value = input("Enter a number: ")

print(value + " is my favourite number!") #by default inputs are treated as a string

print("When you multiple it by 10, this is what you get: ")
value_int = int(value) 
                        # the int() method converts the argument to a integer type
                        # so that the variable VALUE will later be treated as value_int, an integer
print(value_int * 10)
# print(value * 10) -- like this the result would be a 10 times repetition of our input.