def solution(num_list, n):
    l = len(num_list)    
    row = l // n         
    answer = [[0] * n for _ in range(row)]
    idx = 0
    
    for i in range(row):
        for j in range(n):
            answer[i][j] = num_list[idx]
            idx += 1
            
    return answer