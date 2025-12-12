


def PrintStatementMenu():
    print("\n\t𝑷𝑹𝑰𝑵𝑻 𝑺𝑻𝑨𝑻𝑬𝑴𝑬𝑵𝑻 𝑴𝑬𝑵𝑼")
    print("\t﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    print("1. PRINT STATEMENT DEFINITION\n2. EXAMPLE\n3. BACK TO MAIN MENU")

def PrintStatement():
    print("\n\t\tA print statement in programming refers to an instruction within a program that causes data to be displayed to an output device," 
        " \n\t\ttypically the console or a file. It allows programmers to output text, variable values, or other objects," 
        " \n\t\tallowing them to see the results of operations, track program execution, or debug issues.")
    
def ExamplePrint():
    print("\n#Basic Print Statement")
    print('Input: print("Hello, World!")\nOutput: Hello, World!')
    print('\n#Print a sentence\nInput: print("Welcome to my Python Interactive Menu Program!")\
          \nOutput: Welcome to my Python Interactive Menu Program!\n\n#Print using variables\
          \nname = "Oswald"\nInput: print("Hello,", name)\nOutput: Hello, Oswald\n\n#Print with formatting\
          \nage = 21\nInput: print(f"I am {age} years old.")\nOutput: I am 21 years old.')
    


def VariablesMenu():
    print("\n\t𝑽𝑨𝑹𝑰𝑨𝑩𝑳𝑬𝑺 𝑴𝑬𝑵𝑼")
    print("\t﹌﹌﹌﹌﹌﹌﹌")
    print("1. VARIABLES DEFINITION\n2. EXAMPLE\n3. BACK TO MAIN MENU")

def VariablesDefinition():
    print("\t\tIn Python, variables are symbolic names (labels) that refer to objects stored in memory. " \
    "\n\t\tThey are used as containers to store data values (like numbers, strings, or lists) " \
    "\n\t\tso that the data can be referenced and manipulated throughout a program's execution.")

def ExampleVaria():
    print('#Assigning a value to a variable\nname = "Oswald"\n\n#Storing a number\nage = 18')
    print("\n#Changing a variable's value \nx = 10\nx = 20")
    print('\n#Different data types\nstudent_name = "Oswald"\
         #string\ngrade = 95\t\t\t#integer\nheight = 5.7\
         \t\t#float\nis_passed = True\t\t#boolean\n\n#Using variables inside print\
         \nname = "Oswald"\nage = 21\nExample Input: print("My name is", name, "and I am", age, "years old.")\
         \nExample Output: My name is Oswald and I am 21 years old.\
         \n\n#Using user input as a variable\nloc_city = input("Enter your city: ")\
         \nprint("You live in", loc_city)\nExample: Enter your city: Lucena\nOutput: You live in Lucena')
    


def OperatorsMenu():
    print("\n\t𝑶𝑷𝑬𝑹𝑨𝑻𝑶𝑹𝑺 𝑴𝑬𝑵𝑼")
    print("\t﹌﹌﹌﹌﹌﹌﹌")
    print("1. OPERATORS DEFINITION\n2. EXAMPLE\n3. BACK TO MAIN MENU")

def OperatorsDefinition():
    print("\t\tA variable is a characteristic, number, quantity, or symbol that can be measured,\
           \n\t\tcounted, or changed, meaning it does not have a fixed value.\
           \n\t\tThe concept and its definition vary slightly depending on the context,\
           \n\t\tsuch as in mathematics, scientific research, or computer programming.")
    
def OperatorsExample():
    print('#Arithmetic Operators\nx = 10\ny = 3\n\nprint(x + y) \
       \t#Addition → 13\nprint(x - y)\t\t#Subtraction → 7\nprint(x * y) \
       \t#Multiplication → 30\nprint(x / y)\t\t#Division → 3.333...\nprint(x % y) \
       \t#Modulus → 1\nprint(x ** y)\t\t#Exponent → 1000\n\n#Comparison Operators\na = 5\nb = 8\n\nprint(a > b)   # False\
       \nprint(a < b)   # True\nprint(a == b)  # False\nprint(a != b)  # True\n\n#Logical Operators\nage = 18\nis_student = True \
       \n\nprint(age >= 18 and is_student)   # True\nprint(age < 18 or is_student)     # True\nprint(not is_student)             # False \
       \n\n#Assignment Operators\nx = 10\nx += 5   # x = x + 5\nprint(x) # Output: 15\n\nx *= 2   # x = x * 2\nprint(x) # Output: 30 \
       \n\n#User Input + Operator Example\nnum1 = int(input("Enter first number: "))\nnum2 = int(input("Enter second number: ")) \
       \n\nprint("Sum =", num1 + num2)\n\nExample: Enter first number: 20\nExample: Enter second number: 20\nOutput: Sum = 40')
    


def IfElseMenu():
    print("\n\t𝑰𝑭 𝑬𝑳𝑺𝑬 𝑴𝑬𝑵𝑼")
    print("\t﹌﹌﹌﹌﹌﹌")
    print("1. CONDITIONAL STATEMENTS DEFINITION\n2. EXAMPLE\n3. BACK TO MAIN MENU")

def IfElseDefinition():
    print('\t\tConditional statements (also known as control flow statements)\
           \n\t\tare a core part of Python programming that allow a program to make decisions\
           \n\t\tand execute different code blocks based on whether specific conditions are met.\
           \n\t\tThe primary keywords used for this purpose are if, elif (short for "else if"), and else.')
    
def IfElsExample():
    print('#Basic if Statement\nage = 18\nif age >= 18:\n\tprint("You are an adult.")\n\n#if–else Statement\nnum = 5\n\nif num > 0:\
    \n\tprint("The number is positive.")\nelse:\n\tprint("The number is negative.")\n\n#if–elif–else Statement\ngrade = 85\n\nif grade >= 90:\
    \n\tprint("Excellent")\nelif grade >= 75:\n\tprint("Very Good")\nelif grade >= 60:\n\tprint("Good")\nelse:\n\tprint("Needs Improvement")\
    \n\n#Nested if Statement\nage = 20\n\nif age >= 18:\n\tprint("You can enter.")\n\tif age >= 21:\n\t\tprint("You have full access.")\n\telse:\
    \n\t\tprint("Limited access.")\n\n#User Input + Conditional Example\nnumber = int(input("Enter a number: "))\n\nif number % 2 == 0:\
    \n\tprint("The number is even.")\nelse:\n\tprint("The number is odd.")')



def LoopsMenu():
    print("\n\t𝑳𝑶𝑶𝑷𝑺 (𝒇𝒐𝒓 𝒂𝒏𝒅 𝒘𝒉𝒊𝒍𝒆) 𝑴𝑬𝑵𝑼")
    print("\t﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    print("1. LOOPS (for and while) DEFINITION\n2. EXAMPLE\n3. BACK TO MAIN MENU")

def LoopsDefinition():
    print("\t\tA for loop is used when you know the number of times to iterate,\
           \n\t\twhile a while loop is used when you don't know in advance\
           \n\t\tand need to repeat a block of code as long as a condition remains true.\
           \n\t\tFor loops are ideal for iterating over a sequence of items,\
           \n\t\twhile while loops are better for repeating a task\
           \n\t\tuntil a specific condition is met or an event occurs. ")

def LoopsExample():
    print('#for Loop\n#Basic for loop\nfor i in range(5):\n\tprint(i)\n\n#Output:\n0\n1\n2\n3\n4\n\n#Loop through a list\nfruits = ["apple", "banana", "mango"]\
          \n\nfor fruit in fruits:\n\tprint(fruit)\n#for loop with start and end\nfor num in range(1, 6):\n\tprint(num)\n\n#while Loop\n#Basic while loop\
          \ncount = 1\n\nwhile count <= 5:\n\tprint(count)\n\tcount += 1\n\n#while loop until user stops\nanswer = ""\
          \n\nwhile answer != "stop":\n\tanswer = input("Type "stop" to end: ")\n\n#Countdown using while\nnum = 5\n\nwhile num > 0:\n\tprint(num)\
          \n\tnum -= 1\n\n# Loop with break\nfor i in range(10):\n\tif i == 5:\n\t\tbreak\n\tprint(i)\n\n# Loop with continue\nfor i in range(5):\
          \n\tif i == 2:\n\t\tcontinue\n\tprint(i)\n\n# User Input + Loop Example\nlimit = int(input("Enter a number: "))\n\nfor i in range(1, limit + 1):\n\tprint(i)')
    


def ListMenu():
    print("\n\t𝑳𝑰𝑺𝑻 𝑴𝑬𝑵𝑼")
    print("\t﹌﹌﹌﹌﹌")
    print("1. LIST DEFINITION\n2. EXAMPLE\n3. BACK TO MAIN MENU")

def ListDefinition():
    print("\t\tIn Python, a list is a fundamental, built-in data type used to store an ordered collection \
          \n\t\tof items. It is characterized by the following properties:\n\n\t\tOrdered: The items in a list maintain a specific order, and this order is preserved \
          \n\t\twhen the list is accessed or modified. Each item can be accessed by its index, \
          \n\t\tstarting from 0 for the first element.\n\n\t\tChangeable (Mutable): Lists are mutable, meaning their elements can be added, \
          \n\t\tremoved, or modified after the list has been created.\n\n\t\tAllows Duplicate Values: Lists can contain multiple occurrences of the same item.\
          \n\n\t\tHeterogeneous:Lists can store items of different data types within the same list \n\t\t(e.g., integers, strings, floats, booleans, or even other lists).\
           \n\n\t\tDefined with Square Brackets: Lists are created by enclosing the items within \n\t\tsquare brackets [], with items separated by commas.")

def ListExample():
    print('''\n#Creating a List\nfruits = ["apple", "banana", "mango"]\nprint(fruits)\n\n#Accessing Elements\nfruits = ["apple", "banana", "mango"]\nprint(fruits[0])   #apple\
          \nprint(fruits[2])   #mango\n\n#Modifying Elements\nfruits = ["apple", "banana", "mango"]\nfruits[1] = "orange"\nprint(fruits)      #['apple', 'orange', 'mango']\
          \n\n#Adding Elements\nfruits = ["apple", "banana"]\nfruits.append("mango")      #Add at the end\nfruits.insert(1, "orange")  #Add at index 1\
          \nprint(fruits)               #['apple', 'orange', 'banana', 'mango']\n\n#Removing Elements\nfruits = ["apple", "banana", "mango"]\nfruits.remove("banana")   #Remove by value\
          \ndel fruits[0]             #Remove by index\npopped = fruits.pop()     #Remove last element\nprint(fruits)\nprint("Popped:", popped)\n\n#Looping Through a List\
          \nfruits = ["apple", "banana", "mango"]\n\nfor fruit in fruits:\n\tprint(fruit)\n\n#List Operations\nnumbers = [1, 2, 3]\nmore_numbers = [4, 5]\
          \nall_numbers = numbers + more_numbers   #Concatenate lists\nprint(all_numbers)\nprint(len(all_numbers))                #Length of list\n\n#User Input + List Example\
          \nmy_list = []\nn = int(input("How many items do you want to add? "))\n\nfor i in range(n):\n\titem = input("Enter item: ")\n\tmy_list.append(item)\n\nprint("Your list:", my_list)''')
    


def FunctionsMenu():
    print("\n\t𝑭𝑼𝑵𝑪𝑻𝑰𝑶𝑵𝑺 𝑴𝑬𝑵𝑼")
    print("\t﹌﹌﹌﹌﹌﹌")
    print("1. FUNCTIONS DEFINITION\n2. EXAMPLE\n3. BACK TO MAIN MENU")

def FunctionsDefinition():
    print("\t\tA function in Python is a block of reusable code that performs a specific task.\n\t\tInstead of writing the same code again and again,\
           \n\t\tyou place it inside a function and call it whenever you need it.")

def FunctionsExample():
    print('#Defining a Simple Function\ndef greet():\n\tprint("Hello! Welcome to Python Functions.")\n\n\n#Usage:\n\ngreet()\n\n#Function with Parameters\
          \ndef greet_name(name):\n\tprint(f"Hello, {name}!")\n\ngreet_name("Oswald")\ndef add_numbers(a, b):\n\treturn a + b\n\nresult = add_numbers(5, 3)\nprint("Sum:", result)\
        \n\n#Function with Default Parameters\ndef greet_person(name="Guest"):\n\tprint(f"Hello, {name}!")\n\ngreet_person()        # Hello, Guest!\n\ngreet_person("Ana")   # Hello, Ana!\
          \n\n#Function with Multiple Parameters\ndef introduce(name, age, city):\n\tprint(f"My name is {name}, I am {age} years old, and I live in {city}.")\n\nintroduce("Oswald", 18, "Manila")\
          \n\n#Function Calling Another Function\ndef square(x):\n\treturn x * x\n\ndef display_square(num):\n\tprint(f"The square of {num} is {square(num)}")\n\ndisplay_square(5)\
          \n\n#User Input + Function Example\ndef multiply(a, b):\n\treturn a * b\n\nnum1 = int(input("Enter first number: "))\nnum2 = int(input("Enter second number: "))\n\nprint("Result:", multiply(num1, num2))')