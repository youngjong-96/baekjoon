def solution(arr):
    answer = 0
    
    for n in arr:
        if n >= 50 and n % 2 == 0:
            cnt = 0
            while n >= 50:
                n /= 2
                cnt += 1
            answer = max(answer, cnt)
        elif n < 50 and n % 2 == 1:
            cnt = 0
            while n < 50:
                n = n * 2 + 1
                cnt += 1
            answer = max(answer, cnt)
            
    return answer