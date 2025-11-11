array = [1, -2, 3, -4, 5]
print("Массив:", array)
def check_alternating_signs(arr):
    if len(arr) < 2:
        return True  
    for i in range(len(arr) - 1):
        if (arr[i] >= 0) == (arr[i + 1] >= 0):
            return False
    return True
