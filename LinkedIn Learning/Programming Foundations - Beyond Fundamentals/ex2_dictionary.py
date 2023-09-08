# To create a dictionary we will create use the following structure:
# dictionaryname = {LABEL0:item0, LABEL1:item1}

food = {"appetizer":"hummus","entree":"gyro wraps","dessert":"baklava"}
# We use dictionaries to label elements, allowing to store related information.

california_symbols = {
    "bird":"California quail",
    "animal":"Grizzly bear",
    "flower":"California poppy",
    "fruit":"Avocado"
}

# How to access items in a dictionary? We need to supply the label

print(california_symbols["animal"])

# Python's lists and dictionaries can have their elements changed, they are mutable. In other languages this is not so.
# In Python a tupple is a list that can not be changed.