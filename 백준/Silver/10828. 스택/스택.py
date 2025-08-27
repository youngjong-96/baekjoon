# 스택

"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys

stack = [0] * 10000
p = -1

def push(n):
    global p
    p += 1
    stack[p] = n

def pop():
    global p
    if p == -1:
        return -1
    else:
        p -= 1
        return stack[p+1]

def size():
    global p
    return p+1

def empty():
    global p
    if p == -1:
        return 1
    else:
        return 0

def top():
    global p
    if p == -1:
        return -1
    else:
        return stack[p]

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
n = int(sys.stdin.readline())
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
for _ in range(n):
    command = list(map(str, sys.stdin.readline().strip().split()))

    if len(command) > 1:
        push(command[1])
    else:
        if command[0] == 'pop':
            print(pop())
        elif command[0] == 'size':
            print(size())
        elif command[0] == 'empty':
            print(empty())
        elif command[0] == 'top':
            print(top())
