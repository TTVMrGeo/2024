def sum_array(arr):
    return 0 if arr == None or len(arr) < 3 else sum(arr) - max(arr) - min(arr)
print(sum_array([1, 2, 3, 4, 5]))