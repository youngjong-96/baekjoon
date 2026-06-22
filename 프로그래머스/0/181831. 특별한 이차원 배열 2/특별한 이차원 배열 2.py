def solution(arr):
    n = len(arr)
    answer = 1
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                answer = 0
                break
                
    return answer