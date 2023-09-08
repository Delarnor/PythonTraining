miles = input ("Enter a distance in Miles: ")
#kilometers_value = miles_value * 1.609344

# TASK: take an input from the user, convert it to kilometers
# Print the result to the terminal with a text description

kilometers_value = float(miles) * 1.609344 # we create a new variable that equals to the transformed input * the value

print(str(miles) + " miles correspond to " + str(kilometers_value) + " kilometers.")