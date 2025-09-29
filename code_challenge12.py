for i in range(7):
    for x in range(6, i, -1):
        print(" ", end = " ")
    for y in range(i, 0, -1):
        print(y, end =" ")
    for me in range(2, i + 1, 1):
        print(me, end=" ")
    print()