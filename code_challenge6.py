#ODD NUMBER SUMNATION
#Enter 7 random numbers, get the sumnation of all number given


odd = 0
for x in range(1, 8, 1):
    num = eval(input(f"{x}.Enter a number: "))
    if num % 2:
        odd += num
print("The sum of all given odd numbers is:", odd)
