def solution(s):
    answer = []
    letters = []
    for l in s:
        if s.count(l) == 1:
            letters.append(l)
    
    return "".join(sorted(letters))