def solution(emergency):
    l = len(emergency)
    lst = [(value, idx) for idx, value in enumerate(emergency)]
    lst.sort(reverse=True)
    result = [0] * l
    
    for number, data in enumerate(lst):
        result[data[1]] = number + 1
        
    return result