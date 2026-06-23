def solution(arr):
    row = len(arr)
    col = len(arr[0])
    
    if row < col:
        for _ in range(col - row):
            arr.append([0] * col)
    elif col < row:
        for r in arr:
            for _ in range(row - col):
                r.append(0)
    
    return arr