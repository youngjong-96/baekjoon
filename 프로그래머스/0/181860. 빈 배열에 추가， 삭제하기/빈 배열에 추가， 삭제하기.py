def solution(arr, flag):
    answer = []
    l = len(arr)
    
    for i in range(l):
        if flag[i]:
            answer.extend([arr[i]] * (arr[i] * 2))
        else:
            answer = answer[:-arr[i]]
            
    return answer