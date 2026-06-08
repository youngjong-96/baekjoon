def solution(arr, idx):
    answer = -1
    l = len(arr)
    
    for i in range(idx, l):
        if arr[i]:
            answer = i
            break
            
    return answer