# 3.2.4   LAB   Guess the secret number

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

answer = int(input("Your answer: "))

while answer != secret_number:
    print("Ha ha! You're stuck in my loop!")
    answer = int(input("Give me another: "))
print("Well done, muggle! You are free now.")
