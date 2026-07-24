def check(n, s):
    if n % s == 0:
        return 1
    else:
        return 0
    
def solution(n, numlist):
    answer = []
    for num in numlist:
        if check(num, n):
            answer.append(num)
    return answer