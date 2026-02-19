import sys


input = sys.stdin.readline

left = list(input().strip())
right = [] 

M = int(input().strip())

for _ in range(M):
    C = input().split()
    
    if C[0] == 'L':
        if left:
            right.append(left.pop())
            
    elif C[0] == 'D':
        if right:
            left.append(right.pop())
            
    elif C[0] == 'B':
        if left:
            left.pop() 
            
    elif C[0] == 'P':
        left.append(C[1]) 

print("".join(left) + "".join(reversed(right)))