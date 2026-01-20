import sys
from heapq import heappush, heappop

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    heap = [] # 최소힙
    heap_max = [] # 최대힙
    k = int(input().strip())
    visited = [0] * k

    for i in range(k):
        # 명령, 정수
        c, n = input().split()
        n = int(n)

        # 삽입
        if c == 'I':
            heappush(heap, (n, i)) # 최소힙
            heappush(heap_max, (-n, i)) # 최대힙
            visited[i] = True

        # 삭제
        elif c == 'D':
            if n == 1: # 최댓값 삭제
                while heap_max and not visited[heap_max[0][1]]:
                    heappop(heap_max)
                if heap_max:
                    visited[heap_max[0][1]] = False
                    heappop(heap_max)
            elif n == -1: # 최솟값 삭제
                while heap and not visited[heap[0][1]]:
                    heappop(heap)
                if heap:
                    visited[heap[0][1]] = False
                    heappop(heap)
        
        # 동기화
        while heap and not visited[heap[0][1]]:
            heappop(heap)
        while heap_max and not visited[heap_max[0][1]]:
            heappop(heap_max)
        
    if not heap:
        print('EMPTY')
    else:
        print(-heap_max[0][0], heap[0][0])