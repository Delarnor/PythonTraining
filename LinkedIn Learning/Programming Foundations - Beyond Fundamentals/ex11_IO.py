infile = open("values.txt","rt")              # these lines open the mentioned files, located in the same folder.
outfile = open("values-totaled.txt","wt")     # if the file doesn't exist, python will create them.
print('Processing input')                     # Just a message to the user, gives feedback on the process.
sum = 0                                       # we define a variable that will be used to iteration

for line in infile:
    sum = sum + int(line)                     # We convert variable LINE to allow it to work as number
    print(line.rstrip(), file = outfile)      # While we iterate, it will write in the outfile each character
print('\nTotal: ' + str(sum), file = outfile) # In a new line, it will write the sum value of all numbers.
outfile.close()                               # closes the 'outfile'.
print("Output complete")                      # Final feedback to the user.