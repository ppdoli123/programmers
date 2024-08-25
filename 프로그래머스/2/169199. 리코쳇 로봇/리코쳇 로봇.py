from collections import deque

def solution(board):
    width = len(board[0])
    height = len(board)
    dimension = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # 시작점 ('R')과 목표점 ('G') 찾기
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for i in range(height):
        for j in range(width):
            if board[i][j] == "R":
                start_x, start_y = i, j
            if board[i][j] == "G":
                end_x, end_y = i, j
    
    # BFS 큐 초기화 (현재 위치와 이동 횟수 포함)
    queue = deque([(start_x, start_y, 0)])
    visited = set()
    visited.add((start_x, start_y))
    
    while queue:
        current_x, current_y, moves = queue.popleft()
        
        # 목표 지점에 도달했는지 확인
        if board[current_x][current_y] == "G":
            return moves
        
        # 네 방향으로 탐색
        for dx, dy in dimension:
            nx, ny = current_x, current_y
            
            # 벽이나 장애물 'D'를 만날 때까지 현재 방향으로 이동
            while 0 <= nx + dx < height and 0 <= ny + dy < width and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            
            # 새로운 위치가 방문된 적이 없다면 큐에 추가
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
    
    # 경로를 찾지 못한 경우
    return -1
