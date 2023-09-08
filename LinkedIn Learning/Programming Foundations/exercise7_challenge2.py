# Has a function named favourite_city
# The favourite_city should one parameter: name
# You should call favourite_city at least three times
# The output should inclide: "One of my favourite cities is "

def favourite_city(name,famous,dish):
    print("One of my favourite cities is " + str(name))
    print("It is know for its" + str(famous))
    print("The most popular dish in "+ name +" is "+ str(dish))

# print("What's one of your favourite cities? ")
name = input("What's one of your favourite cities? ")
print()
famous = input("What is it famous for? ")
print("")
dish = input ("When it comes to food, the best known dish is: ")
print("")
favourite_city(name,famous,dish)