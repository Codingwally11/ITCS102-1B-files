#Ask user to input 10 numbers
#After get the sumation of all number
sum = 0
for x in range(1, 11, 1):
    print(x)
    number = eval(input("Enter any Number--->> "))
    sum += number
print("The sumation of all number is:", sum)