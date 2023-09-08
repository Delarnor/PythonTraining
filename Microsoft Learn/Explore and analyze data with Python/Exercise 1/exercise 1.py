# https://learn.microsoft.com/en-gb/training/modules/explore-analyze-data-with-python/3-exercise-explore-data

# Let's start by looking at some simple data.
# Suppose a college professor takes a sample of student grades from a class to analyze.

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)

# The data has been loaded into a Python list structure, 
# which is a good data type for general data manipulation, but it's not optimized for numeric analysis. 
# For that, we're going to use the NumPy package, 
# which includes specific data types and functions for working with Numbers in Python.
# Run the following cell to load the data into a NumPy array.
