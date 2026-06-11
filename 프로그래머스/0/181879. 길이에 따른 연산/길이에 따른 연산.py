def solution(num_list):
    answer = 0
    l = len(num_list)
    
    if l >= 11:
        for n in num_list:
            answer += n
    else:
        answer = 1
        for n in num_list:
            answer *= n
            
    return answer