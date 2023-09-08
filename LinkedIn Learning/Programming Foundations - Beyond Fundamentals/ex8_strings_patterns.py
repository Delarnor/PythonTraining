# Start code:
# firstname = "malala"
# lastname = "yousafzai"
# note = "award: Nobel Peace Prize"

# We asked users to fill our form but they used lower case.
# We will capitalize() it like this:

    # We define a variable and assign it a string.
    # Then we use that same variable.capitalize() and then we will print the new variable:

firstname = "malala"
lastname = "yousafzai"
note = "award: Nobel Peace Prize"

firstnamecap = firstname.capitalize()
lastnamecap = lastname.capitalize()

print(firstnamecap)
print(lastnamecap)

print("")

# To search for particular characters in a string we can also use these methods:

# .find() -> gives a ref. to the first occurence.
# .index() -> gives a ref. to the first occurence.

# .rfind() -> gives a ref. to the last occurence.
# .rinfex() -> gives a ref. to the last occurence.

awardlocation = note.find("award: ") # finds the location (numeric position) in the note variable
print(awardlocation) # output is 0

# In python getting part of a string is called slicing: string[start:end] (if we remove either start or
# end, the search continues beyond)

awardtext = note[7:] # this means the variable starts at postion 7 of the "note" variable
print(awardtext)
