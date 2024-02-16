def solution(board):
    stack = [[0, 0, 'START']] # y, x, direction
    size = len(board)
    board[0][0] = -500
    while stack:
        y, x, direction = stack.pop()
        cost = board[y][x]
        for dy, dx, drt in [(-1, 0, 'U'), (0, -1, 'L'), (1, 0, 'D'), (0, 1, 'R',)]:
            ny, nx = y + dy, x + dx
            c = 0
            if 0 <= ny < size and 0 <= nx < size:
                if board[ny][nx] != 1:
                    c += 100
                    if direction != drt:
                        c += 500
                    if board[ny][nx] == 0 or board[ny][nx] >= cost + c:
                        board[ny][nx] = cost+c
                        stack.append([ny, nx, drt])
    return board[-1][-1]  