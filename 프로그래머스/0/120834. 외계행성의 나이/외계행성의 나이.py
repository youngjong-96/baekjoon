def solution(age):
    lst = list(str(age))
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
            'w','x','y','z']
    
    for s in lst:
        answer += alpha[int(s)]
    
    return answer