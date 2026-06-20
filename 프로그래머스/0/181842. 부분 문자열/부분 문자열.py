def solution(str1, str2):
    s1 = len(str1)
    s2 = len(str2)
    answer = 0
    
    for i in range(s2):
        if str2[i:i+s1] == str1:
            answer = 1
            break
    
    return answer