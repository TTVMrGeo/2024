array = [1, 5, 2, 7, 9, 12, 551, 0]

swapped = True
while swapped:
    swapped = False
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
            swapped = True
            
print(array)