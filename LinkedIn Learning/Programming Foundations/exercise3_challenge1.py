# Instructions
# 1) Ask the user: What's my favourite food?
# 2) If user enters my favourite food, output: "Yep! So amazing!"
# 3) If the user does not enter my favourite food, the output: "Yuck, that's not it!"
# 4) Regardless of the user input, finish with: "Thanks for playing!"

favouritefood = "Sushi"

# On the video she used: guess = input("What's my favourite food? ")

print("What's my favourite food?")

answer = str(input())
print("")

if answer == favouritefood:
    print("Yep! So amazing!")
else:
    print("Yuck, that's not it!")

print("")
print("Thanks for playing!")
