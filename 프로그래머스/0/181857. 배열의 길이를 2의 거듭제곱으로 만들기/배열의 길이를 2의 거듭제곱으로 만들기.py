def solution(arr):
    answer = []
    l = len(arr)
    
    if l <= 2 ** 0:
        answer = arr
    elif l <= 2 ** 1:
        answer = arr + [0] * (2 - l)
    elif l <= 2 ** 2:
        answer = arr + [0] * (2 ** 2  - l)
    elif l <= 2 ** 3:
        answer = arr + [0] * (2 ** 3 - l)
    elif l <= 2 ** 4:
        answer = arr + [0] * (2 ** 4 - l)
    elif l <= 2 ** 5:
        answer = arr + [0] * (2 ** 5 - l)
    elif l <= 2 ** 6:
        answer = arr + [0] * (2 ** 6 - l)
    elif l <= 2 ** 7:
        answer = arr + [0] * (2 ** 7 - l)
    elif l <= 2 ** 8:
        answer = arr + [0] * (2 ** 8 - l)
    elif l <= 2 ** 9:
        answer = arr + [0] * (2 ** 9 - l)
    elif l <= 2 ** 10:
        answer = arr + [0] * (2 ** 10 - l)
        
    return answer