def solution(n):
    # n x n 배열을 0으로 초기화
    answer = [[0] * n for _ in range(n)]
    
    # 우, 하, 좌, 상 순서의 방향 벡터
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 시작 위치 및 초기 방향 (우측)
    x, y, direction = 0, 0, 0
    
    for i in range(1, n * n + 1):
        answer[x][y] = i
        
        # 다음 이동할 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 다음 위치가 배열을 벗어나거나, 이미 숫자가 채워져 있는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            # 방향을 시계방향으로 전환
            direction = (direction + 1) % 4
            # 전환된 방향으로 다시 다음 위치 계산
            nx = x + dx[direction]
            ny = y + dy[direction]
            
        # 현재 위치를 다음 위치로 업데이트
        x, y = nx, ny
        
    return answer