# Regular expression - allows the creattion of description of a pattern we wanna match to. 
# Then we can check a string to that regular expression (REGEX), 
# It can be made of letters, numbers or special characters

# Exemplos:
# /hello/ -> looks for specific text
# \d -> indicates a digit
# \w -> indicates a word character, like a letter
# . -> any characters
# + -> one or more occurences
# * -> 0 or more
# ? -> 0 or 1

import re

five_digit_zip = "98101"
nine_digit_zip = "98101-0003"
phone_number = "213-234-5667"

# Create a way to check if a variable has 5 digit zip code

five_digit_expression = r"\d{5}" # 5 occurrences of the preceding expression, a digit
print(re.search(five_digit_expression,five_digit_zip))
print(re.search(five_digit_expression,nine_digit_zip))
print(re.search(five_digit_expression,phone_number))