def solution(num_list):
    answer = 0
    odd, even = 0, 0
    l = len(num_list)
    
    for i in range(l):
        if i % 2 == 0:
            odd += num_list[i]
        else:
            even += num_list[i]
    
    if odd >= even:
        answer = odd
    else:
        answer = even
        
    return answer