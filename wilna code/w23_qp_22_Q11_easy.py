import math

WoodTypes = ["Laminate", "Pine", "Oak"]
Prices = [29.99, 39.99, 54.99]

for j in range(3):
    print(j+1, WoodTypes[j], "$" + str(Prices[j]))
    
choice = int(input("What type of wood would you like?\n> "))
def length_and_width():
    global length
    global width
    global area
    length = float(input("Enter length between 1.5 and 10 meters\n> "))
    width = float(input("Enter width 1.5 and 10 meters\n> "))
    area = length * width 
    area = math.ceil(area)
    
length_and_width()

if choice == 1:
    price = Prices[0]
elif choice == 2:
    price = Prices[1]
elif choice == 3:
    price = Prices[2]
else:
    print("Invalid choice")


def check_if_valid():
    if length < 1.5 or length > 10 or width < 1.5 or width > 10:
        print("\nThe length or width is not between 1.5 and 10 meters.\n")
        length_and_width()
    else:
        total = area * price
        print(f"\nYou wood will cost ${round(total, 2)}\n")

check_if_valid()