def solution(arr, k):
    answer = []
    l = len(arr)
    i = 0
    
    while len(answer) < k and i < l:
        if arr[i] in answer:
            i += 1
            continue
        answer.append(arr[i])
        i += 1
    
    if len(answer) < k:
        while len(answer) < k:
            answer.append(-1)
            
    return answer