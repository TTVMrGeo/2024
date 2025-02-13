import os

target = str(input("Target: "))
os.system('cls')
user = ""
user = str(input("Your guess: "))
length = len(target)
output = []

target = [*target]
user = [*user]
for i in range(length):
    output.append("-")

for j in range(length):
    if user[j] == target[j]:
        output[j] = "G"
    if user[j] != target[j] and user[j] in target:
        output[j] = "Y"
    else:
        print("Yep! You got it")
    
print(output)