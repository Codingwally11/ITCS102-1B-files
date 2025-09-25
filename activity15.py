#STRING FORMATTING
#STRING CONCATENATION
"""

fname = 'oswald '
mname = ''
lname = 'pastorfide'

print("My full name is ", fname," ", mname, " ", lname)


fname = 'oswald '
mname = ''
lname = 'pastorfide'
print(f"My full name is {fname} {mname} {lname}")


fname = 'oswald '
mname = ''
lname = 'pastorfide'
print(f"My full name is {fname.upper()} {mname.upper()} {lname.upper()}")

"""

sum = 0 
for i in range(1, 6):
    x  = eval(input(f"{i} - Input a number --> "))
    sum += x 
print(f"The total sum is {sum}")