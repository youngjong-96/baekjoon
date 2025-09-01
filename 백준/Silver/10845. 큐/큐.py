# 큐
import sys

queue = [0] * 10000
head, rear = -1, -1

def push(x):
    global rear
    if rear == len(queue):
        print('queue if full')
    else:
        rear += 1
        queue[rear] = x

def pop():
    global head
    if empty():
        return -1
    else:
        head += 1
        return queue[head]

def size():
    global rear
    global head

    return rear - head

def empty():
    if rear == head:
        return 1
    else:
        return 0

def front():
    global head
    if empty():
        return -1
    else:
        return queue[head + 1]

def back():
    global rear
    if empty():
        return -1
    else:
        return queue[rear]


n = int(input())
for _ in range(n):
    order = list(map(str, sys.stdin.readline().strip().split()))

    if len(order) > 1:
        push(int(order[1]))
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'front':
        print(front())
    elif order[0] == 'back':
        print(back())
