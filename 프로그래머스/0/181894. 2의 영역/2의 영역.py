def solution(arr):
    n = arr.count(2)
    l = len(arr)
    
    cnt = 0
    s, e = -1, 0
    for i in range(l):
        if arr[i] == 2:
            cnt += 1
            if s == -1:
                s = i
            if cnt == n:
                e = i
                break
    
    answer = arr[s:e + 1]
    
    if not answer:
        answer = [-1]
        
    return answer