def solution(arr, n):
    l = len(arr)
    
    if l % 2 == 1:
        for i in range(0, l, 2):
            arr[i] += n
    else:
        for i in range(1, l, 2):
            arr[i] += n
            
    return arr