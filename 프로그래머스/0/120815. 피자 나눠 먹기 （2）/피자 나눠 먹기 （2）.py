def solution(n):
    num = max(n, 6)
    m = 1
    
    for i in range(num, 1, -1):
        if n % i == 0 and 6 % i == 0:
            m = i
            break
    
    pieces = m * (n // m) * (6 // m)
    
    return pieces // 6