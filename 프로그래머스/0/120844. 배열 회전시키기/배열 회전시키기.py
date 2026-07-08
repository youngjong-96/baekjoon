def left(arr):
    l = len(arr)
    temp = arr[0]
    
    for i in range(l - 1):
        arr[i] = arr[(i + 1) % l]
    
    arr[-1] = temp
    
    return arr

def right(arr):
    l = len(arr)
    temp = arr[-1]
    
    for i in range(l - 1, 0, -1):
        arr[i] = arr[(i - 1) % l]
    
    arr[0] = temp
    
    return arr

def solution(numbers, direction):
    if direction == 'right':
        return right(numbers)
    else:
        return left(numbers)