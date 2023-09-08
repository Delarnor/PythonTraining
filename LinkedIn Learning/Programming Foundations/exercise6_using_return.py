# Let's use functions that return value
# A return statement consists of the RETURN keyword and a value (variable) to be returned

def withdraw_money(current_balance,amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(100,80)

if(balance <= 50):
    print("We need to make a deposit")
else:
    print("Nothing to see here")