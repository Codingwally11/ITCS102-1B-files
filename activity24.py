from activity24_1 import GreetPersonName,GreetInfo

# Creating or defining your own function
# Code reusability
# Keyword -- def


def GreetPerson():
    print("\nHi visitor, welcome to my first function")
    print("Please browse around")


GreetPersonName('Oswald')
GreetInfo('Oswald', 'Lucena', '21')


while True:
    print("Code compiler program")
    print("A - First Program \nB - Second Program \nC - Exit")
    choice = input("Select from the option -->").lower()

    if choice == 'a':
        GreetPersonName('Oswald')
        continue
    elif choice == 'b':
        GreetInfo('Oswald', 'Lucena', '21')
        continue
    elif choice == 'c':
        print("System Exit")
        break
    else:
        print("Invalid Choice")
        continue