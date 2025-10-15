name = input("What is your name?  ")

print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n")
go = True
sum = 0
odd = "" #string

while go == True:
    num = eval(input("Input a random number -->"))

    if num % 2 == 1:
        print("ODD NUMBER DETECTED, code continues")
        sum += num
        odd += str(num) + " "
    elif num == 0:
        print("Program Stops.!!!")
        break
    else:
        if num % 2 == 0:
            print("EVEN NUMBER DETECTED, code continue")
        else:
            print("Invalid input")
        continue
print(f"\nHi {name}, the sum of all ODD number is {sum}")
print(f"ODD numbers detected included the {odd}")