def victory(r):
    if r == '2':
        return '0'
    elif r == '0':
        return '5'
    else:
        return '2'
    
def solution(rsp):
    answer = ''
    for i in rsp:
        answer += victory(i)
    return answer