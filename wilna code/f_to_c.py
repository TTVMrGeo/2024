what = input("Would you like to\nA. Convert from °C to °F\nor\nB. Convert From °F to °C?\n")

if what == "A" or what == "a":
    c = float(input("What °C would you like to convert? "))
    cf = (c * 9 / 5) + 32
    print(round(cf), "°F")
elif what == "B" or what == "b":
    f = float(input("What °F would you like to convert? "))
    fc = (f - 32) * 5 / 9
    print(round(fc), "°C")
else:
    print("That was not a option!")