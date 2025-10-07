def recur():
    if len(path) == m:
        print(*path)
        return

    last_used_num = 0
    
    for i in range(n):
        if not visited[i]:
            
            if candidates[i] == last_used_num:
                continue

            visited[i] = True
            path.append(candidates[i])

            last_used_num = candidates[i]
            recur()
            path.pop()
            visited[i] = False


n, m = map(int, input().split())
candidates = list(map(int, input().split()))
candidates.sort()  

visited = [False] * n  
path = []  

recur()