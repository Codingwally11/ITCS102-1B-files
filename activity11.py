
temp = eval(input("Enter a Temperatures ---> "))
if temp <= 0:
    print("BELOW FREEZING")

elif temp >= 1 and temp <= 15:
    print("Extremely cold Temperatures")

elif temp >= 16 and temp <= 30:
    print("Cold Temperatures")

elif temp >= 31 and temp <= 38:
    print("Lukewarm Temperatures")

elif temp >= 39 and temp <= 42:
    print("Warm Temperatures")

elif temp >= 43 and temp <= 50:
    print("Hot Temperatures")

elif temp >= 51 and temp <= 60:
    print("Extremely Hot Temperatures")

elif temp >= 61:
    print("Burning Temperatures")

else:
    print("Invalid Temperatures")