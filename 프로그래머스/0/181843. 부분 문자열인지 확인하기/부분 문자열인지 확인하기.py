def solution(my_string, target):
    l = len(my_string)
    t = len(target)
    answer = 0
    
    for i in range(l):
        if my_string[i:i+t] == target:
            answer = 1
            break
    
    return answer