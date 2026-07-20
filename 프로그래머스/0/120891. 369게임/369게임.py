def solution(order):
    lst = []
    for s in str(order):
        lst.append(s)
    answer = lst.count('3') + lst.count('6') + lst.count('9')
    return answer