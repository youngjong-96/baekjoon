def solution(num_list):
    answer = -1
    l = len(num_list)
    
    for i in range(l):
        if num_list[i] < 0:
            answer = i
            break
        
    return answer