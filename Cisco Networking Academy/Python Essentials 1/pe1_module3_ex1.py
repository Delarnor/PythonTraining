# let's find the largest of three numbers

number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))
number3 = int(input("Give me the third number: "))

bigger_number = number1

if bigger_number < number2:
    bigger_number = number2

if bigger_number < number3:
    bigger_number = number3

print("\nThe biggest number is:",str(bigger_number) +".")