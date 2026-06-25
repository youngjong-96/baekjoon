def solution(arr):
    answer = [arr[0]]
    l = len(arr)
    
    for i in range(1, l):
        if arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])
            
    return answer