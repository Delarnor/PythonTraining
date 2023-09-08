# Debugging is the process of finding and fixing errors

# Syntax Errors - includes code that doesn't belong to that programming language

# Run-time Errors - interpreter fails to execute some or part of the code

# Logic Errors - the code runs but doesn't do so as expected

# Test Cases - set of cases, code used to text another code

def plant_recommendation(care):
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')

plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')
