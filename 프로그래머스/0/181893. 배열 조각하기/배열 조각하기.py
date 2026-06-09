def solution(arr, query):
    l = len(query)
    
    for i in range(l):
        if i % 2 == 0:
            arr = arr[:query[i] + 1]
        else:
            arr = arr[query[i]:]
            
    return arr