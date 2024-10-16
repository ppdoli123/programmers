import sys
sys.setrecursionlimit(10**6)
def solution(maps):
    answer = []
    rows = len(maps)
    columns = len(maps[0])
    checked = [[True for _ in range(columns)] for _ in range(rows)]
    def process(x,y,answer):
        checked[x][y] = False
        dimension = [[1,0],[-1,0],[0,1],[0,-1]]
        for dx,dy in dimension:
            nx,ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < columns:
                if maps[nx][ny] != "X" and checked[nx][ny]:
                    answer += int(maps[nx][ny])
                    answer = process(nx,ny,answer)
        
        return answer
    
    for row in range(rows):
        for column in range(columns):
            if maps[row][column] != "X" and checked[row][column]:
                answer.append(process(row,column,int(maps[row][column])))
                
    if len(answer) == 0 :
        return [-1]
    else:
        answer.sort()           
    return answer