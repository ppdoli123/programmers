from collections import deque

def solution(maps):
    height, width = len(maps), len(maps[0])
    
    # 시작 위치 찾기
    start = next((i, j) for i, row in enumerate(maps) for j, cell in enumerate(row) if cell == 'S')
    
    def bfs(start, end_char):
        queue = deque([(start[0], start[1], 0)])  # x, y, distance
        visited = set([start])
        
        while queue:
            x, y, dist = queue.popleft()
            
            if maps[x][y] == end_char:
                return x, y, dist
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < height and 0 <= ny < width and maps[nx][ny] != 'X' and (nx, ny) not in visited:
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
        
        return None
    
    # 시작 위치에서 레버까지
    lever_result = bfs(start, 'L')
    if not lever_result:
        return -1
    
    # 레버에서 출구까지
    exit_result = bfs((lever_result[0], lever_result[1]), 'E')
    if not exit_result:
        return -1
    
    return lever_result[2] + exit_result[2]