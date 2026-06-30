def solution(num_list):
    answer = []
    odd = 0
    even = 0
    
    for n in num_list:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    
    answer.append(even)
    answer.append(odd)
    
    return answer