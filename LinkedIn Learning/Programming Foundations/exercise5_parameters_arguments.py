# Parameters/Arguments allow functions to work differently based on the input received
print("How much did you payed for? Options are 6 or 12... ")
amount_paid = int(input()) #This states that the variable which will be used as an argument
                            #is of type int and will be created by the user.

print("") # just for space

def wash_car(amount_paid): #created function that uses created variable as argument
    if (amount_paid == 12):
        print("Wash with tri-colour foam")
        print("Rinse twice")
        print("Dry with the large blow dryer")
    if (amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry")

wash_car(amount_paid) # calls the function

print("")
print("Coming right up, thank you for your preference.")