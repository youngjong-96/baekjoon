def solution(keyinput, board):
    x, y = 0, 0
    delta = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}
    boardx = board[0] // 2
    boardy = board[1] // 2
    
    for move in keyinput:
        dx, dy = delta[move]
        if -boardx <= x + dx <= boardx:
            x += dx
        if -boardy <= y + dy <= boardy:
            y += dy
    return [x, y]
    