def solution(myString):
    answer = ''
    for s in myString:
        if s == 'A':
            answer += s
        elif s == 'a':
            answer += s.upper()
        else:
            answer += s.lower()
    return answer