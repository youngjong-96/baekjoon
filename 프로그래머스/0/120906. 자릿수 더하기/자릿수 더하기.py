def solution(n):
    lst = []
    while n > 0:
        lst.append(n % 10)
        n //= 10
    
    return sum(lst)