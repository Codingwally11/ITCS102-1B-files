from menu import * #* = all
import time
import os

name = input("\nWhat is your name? --> ").upper()
loc = input("Where are you from? --> ").upper()
os.system('cls')
print(f"\nHi {name}, from {loc}, welcome to my FINALS PROJECT!")
print("\n𝙋𝙮𝙩𝙝𝙤𝙣 𝙁𝙪𝙣𝙙𝙖𝙢𝙚𝙣𝙩𝙖𝙡𝙨 - 𝙄𝙣𝙩𝙚𝙧𝙖𝙘𝙩𝙞𝙫𝙚 𝙈𝙚𝙣𝙪 𝙋𝙧𝙤𝙜𝙧𝙖𝙢")

main_menu = {}

while True:
    time.sleep(0.3)
    print("\n\t\t=== 𝑴𝑨𝑰𝑵 𝑴𝑬𝑵𝑼 ===")
    time.sleep(0.3)
    print("\n𝒮𝐸𝐿𝐸𝒞𝒯 𝐹𝑅𝒪𝑀 𝒯𝐻𝐸 𝐹𝒪𝐿𝐿𝒪𝒲𝐼𝒩𝒢 𝒪𝒫𝒯𝐼𝒪𝒩")
    time.sleep(0.3)
    print("A - Print Statements")
    time.sleep(0.3)
    print("B - Variables")
    time.sleep(0.3)
    print("C - Operators")
    time.sleep(0.3)
    print("D - Conditional Statements (if, elif, else)")
    time.sleep(0.3)
    print("E - Loops (for and while)")
    time.sleep(0.3)
    print("F - list")
    time.sleep(0.3)
    print("G - Functions")
    time.sleep(0.3)
    print("H - Exit System")
    

    option = input("SELECT FROM THE OPTIONS ABOVE --->").lower()

    if option == 'a': #Print Statement Menu
        os.system('cls')
        while True:
            PrintStatementMenu()

            printS = input("\nSelect from the following number-->").lower()
            if printS == '1':
                os.system('cls')

                PrintStatement()
                continue

            elif printS == '2':
                os.system('cls')
                ExamplePrint()
                continue
                
            elif printS == '3':
                os.system('cls')
                break

            else:
                os.system('cls')
                print("INVALID CHOICE, TRY AGAIN!")
                continue
        continue

    elif option == 'b': #Variables
        os.system('cls')
        while True:
            VariablesMenu()

            varia = input("\nSelect from the following number-->").lower()

            if varia == '1':
                os.system('cls')
                VariablesDefinition()

            elif varia == '2':
                os.system('cls')
                ExampleVaria()
                continue

            elif varia == '3':
                os.system('cls')
                break

            else:
                os.system('cls')
                print("INVALID CHOICE, TRY AGAIN!")
        continue
    
    elif option == 'c': #Operators
        os.system('cls')
        while True:
            OperatorsMenu()

            operate = input("\nSelect from the following number-->").lower()

            if operate == '1':
                os.system('cls')
                OperatorsDefinition()

            elif operate == '2':
                os.system('cls')
                OperatorsExample()
                continue

            elif operate == '3':
                os.system('cls')
                break

            else:
                os.system('cls')
                print("INVALID CHOICE, TRY AGAIN!")
                continue
        continue

    elif option == 'd': #Conditional Statements (if, elif, else)
        os.system('cls')
        while True:
            IfElseMenu()
            
            if_else = input("\nSelect from the following number-->").lower()

            if if_else == '1':
                os.system('cls')
                IfElseDefinition()
                continue

            elif if_else == '2':
                os.system('cls')
                IfElsExample()
                continue

            elif if_else =='3':
                os.system('cls')
                break

            else:
                os.system('cls')
                print("INVALID CHOICE, TRY AGAIN!")
                continue
                
        continue

    elif option == 'e': #Loops (for and while)
        os.system('cls')
        while True:
            LoopsMenu()
            
            loop = input("\nSelect from the following number-->").lower()

            if loop == '1':
                os.system('cls')
                LoopsDefinition()
                continue

            elif loop == '2':
                os.system('cls')
                LoopsExample()
                continue

            elif loop =='3':
                os.system('cls')
                break

            else:
                os.system('cls')
                print("INVALID CHOICE, TRY AGAIN!")
                continue
        continue

    elif option == 'f': #list
        os.system('cls')
        while True:
            ListMenu()
            
            list = input("\nSelect from the following number-->").lower()

            if list == '1':
                os.system('cls')
                ListDefinition()
                continue

            elif list == '2':
                os.system('cls')
                ListExample()
                continue

            elif list =='3':
                os.system('cls')
                break

            else:
                os.system('cls')
                print("INVALID CHOICE, TRY AGAIN!")
                continue
        continue

    elif option == 'g': #Functions
        os.system('cls')
        while True:
            FunctionsMenu()
            
            Funct = input("\nSelect from the following number-->").lower()

            if Funct == '1':
                os.system('cls')
                FunctionsDefinition()
                continue

            elif Funct == '2':
                os.system('cls')
                FunctionsExample()
                continue

            elif Funct =='3':
                os.system('cls')
                break

            else:
                os.system('cls')
                print("INVALID CHOICE, TRY AGAIN!")
                continue
        continue

    elif option == 'h': #Exit
        os.system('cls')
        break

    else:
        os.system('cls')
        print("INVALID OPTION, TRY AGAIN!")
        continue