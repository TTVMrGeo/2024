a = round((int(input("What mark did you get for the test? (out of 60) "))/60) * 100); print(f"You got {a}%")
if a >= 90: print("You got an A*")
elif a >= 80: print("You got an A")
elif a >= 70: print("You got a B")
elif a >= 60: print("You got a C")
elif a >= 50: print("You got a D")
elif a >= 40: print("You got a E")
elif a < 40: print("You got a U")