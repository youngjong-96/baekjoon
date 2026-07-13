def solution(box, n):
    w, v, h = box
    w //= n
    v //= n
    h //= n
    
    return w * v * h