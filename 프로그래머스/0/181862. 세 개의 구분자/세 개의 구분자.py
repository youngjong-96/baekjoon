def solution(myStr):
    answer = []
    Str = ''
    
    for s in myStr:
        if s in ['a', 'b', 'c']:
            if Str != '':
                answer.append(Str)
                Str = ''
        else:
            Str += s
    
    if Str != '':
        answer.append(Str)
    else:
        answer = ["EMPTY"]
            
    return answer