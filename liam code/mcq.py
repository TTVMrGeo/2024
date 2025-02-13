score = 0

first = input("How old is Factorio?\na) 8\nb) 12\nc) 16\nd) 20\n> ")
if first == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
second = input("What is the world record for the amount of players in one Factorio game?\na) 20\nb) over 600\nc) 4\nd) less than 100\n> ")
if second == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
third = input("How long does it take (on average) to beat Factorio?\na) 100h\nb) 10h\nc) 50h\nd) 200h\n> ")
if third == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
fourth = input("How much does factorio cost?\na) R100\nb) R20\nc) R300\nd) R200\n> ")
if fourth == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
fith = input("What is the most popular factorio mod?\na) Factorio Space Age\nb) Krastorio\nc) Alien Biomes\nd) The Cube\n> ")
if fith == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("Your score is " + str(score) + "/5")
if score >= 4:
    print("You are a true factorio player!")
else:
    print("You are not a true factorio player!")