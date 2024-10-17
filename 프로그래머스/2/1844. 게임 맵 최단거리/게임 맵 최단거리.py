from collections import deque 
def solution(maps): 
    global num
    dimension = [[0,1],[0,-1],[1,0],[-1,0]]
    width = len(maps)
    height = len(maps[0])
    visited = [[False for _ in range(height)] for _ in range(width)]
    
    def bfs(que,visited):
        global num
        while que:
            x,y = que.popleft()
            if x == width -1 and y == height -1:
                return maps[-1][-1]
            for dx,dy in dimension :
                nx,ny = x+dx ,y+dy
                if 0 <= nx < width and 0 <= ny < height:
                    if not visited[nx][ny] and maps[nx][ny] == 1:
                        visited[nx][ny] = True
                        que.append([nx,ny])
                        maps[nx][ny] = 1 + maps[x][y]

                    
    que = deque()
    que.append([0,0])
    visited[0][0] = True
    num = 0
    bfs(que,visited)
    if maps[-1][-1] != 1:
        return maps[-1][-1]
    else: 
        return -1
#     #상하좌우 움직임
#     dx=[-1,1,0,0] 
#     dy=[0,0,-1,1]

#     def bfs (x,y):
#         queue=deque()
#         queue.append((x,y)) #큐에 삽입 방문처리는 음..필요없음
#         while queue: #큐가 존재하는 동안 반복
#             x,y=queue.popleft() #꺼낸다음에
#             for i in range(4): #상하좌우 움직여보기
#                 nx=x+dx[i]
#                 ny=y+dy[i]
#                 if 0>nx or 0>ny or nx>=len(maps) or ny>=len(maps[0]): #범위를 벗어난 경우
#                     continue
#                 if maps[nx][ny]==0: #벽인경우
#                     continue
#                 if maps[nx][ny]==1: #길이 있고 위 조건에 해당하지 않는 경우
#                     queue.append((nx,ny)) 
#                     maps[nx][ny]=maps[x][y]+1 #방문처리 동시에 갱신!     
#     bfs(0,0)
#     answer=maps[len(maps)-1][len(maps[0])-1]

#     if answer==1: #도달할 수 없는 경우
#         answer=-1
#     return answer