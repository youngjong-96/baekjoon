def solution(binomial):
    lst = binomial.split()
    a, op, b = int(lst[0]), lst[1], int(lst[2])
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:
        answer = a * b
        
    return answer