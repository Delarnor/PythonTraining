# DRY - a principle for software development meaning Don't Repeat Yourself
# For this, we use FUNCTIONS which are blocks of code group together with a name, 
# for example, the print() function.

# To create a function, let's create one using the DEF (define) statement which lets python know that we
# want to create our own fuction:

# we write: def + function name, open parenthesis, add a variable inside the parenthesis and then 
# add ' : ' as shown below. When we press enter, the next line is indented for us.
def say_hello(name):
    print(f"Hello, {name}!")

# For the function to be used we must call it like this, 
# while adding the variable to be ued in the parenthesis:
say_hello("Johnny")
say_hello("Susy")
say_hello("Mika")