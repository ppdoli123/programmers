import sys
sys.setrecursionlimit(10**6)
def solution(maps):
    answer = []
    height = len(maps)    # 세로 길이
    width = len(maps[0])  # 가로 길이
    
    check = [[False] * width for _ in range(height)]

    def ref(x, y, result):
        check[x][y] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하, 상, 우, 좌
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width and maps[nx][ny] != "X" and not check[nx][ny]:
                result += int(maps[nx][ny])
                result = ref(nx, ny, result)
        
        return result
    
    for i in range(height):
        for j in range(width):
            if maps[i][j] != "X" and not check[i][j]:
                result = ref(i, j, int(maps[i][j]))
                answer.append(result)
                
    # answer.sort()
    return sorted(answer) if answer else [-1]
