def solution(dot):
    x, y = dot
    
    if x > 0 and y > 0:
        answer = 1
    elif x > 0 and y < 0:
        answer = 4
    elif x < 0 and y > 0:
        answer = 2
    else:
        answer = 3
    return answer