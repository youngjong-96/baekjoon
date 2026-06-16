def solution(arr):
    stk = []
    i = 0
    l = len(arr)
    
    while i < l:
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk and stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1
    
    if not stk:
        stk = [-1]
    
    return stk