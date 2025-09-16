number = eval(input("Enter any number---> "))
fact = 1
for x in range(number, 0, -1):
    fact *= x
    print("The Factorial of:",number, "is", fact)