def solution(arr1, arr2):
    a1 = len(arr1)
    a2 = len(arr2)
    
    if a1 > a2:
        answer = 1
    elif a1 < a2:
        answer = -1
    elif a1 == a2 and sum(arr1) > sum(arr2):
        answer = 1
    elif a1 == a2 and sum(arr1) < sum(arr2):
        answer = -1
    else:
        answer = 0
        
    return answer