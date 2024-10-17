from collections import deque
def solution(n,computers):
    visited = [True]*n
    answer = 0
    aa = [0]
    que = deque()
    for i in range(n):
        stack = []
        if visited[i]:
            for j in range(i,n):
                if computers[i][j] == 1:
                    que.append([i,j])
                    visited[i] = False 
                    stack.append(i)
            while que:
                x,y = que.popleft()
                stack.append(y)

                for x in range(n):
                    if  computers[y][x] == 1 and visited[x] and [x,y] not in que:
                        que.append([y,x])
                        computers[y][x] = 0
            if len(set(stack)) != 0 :
                answer +=1
    return answer
#     def dfs(i,visited,ans):
#         if 1 in computers[i][i+1:]:
#             for x in range(i+1,n):
#                 if computers[i][x] == 1 and visited[x]:
#                     visited[x] = False
#                     ans.append(x)
#                     dfs(x,visited,ans)
#         else:
#             aa[0] += 1
#             return aa[0]
#         print(i,visited,aa[0],ans)
        
#     for i in range(n):
#         if visited[i]:
#             ans = [i]
#             dfs(i,visited,ans)
#             print(ans)
# def solution(n, computers):
#     def dfs(node, visited, computers):
#         stack = [node]
#         while stack:
#             current = stack.pop()
#             for neighbor in range(n):
#                 if computers[current][neighbor] == 1 and not visited[neighbor]:
#                     visited[neighbor] = True
#                     stack.append(neighbor)

#     visited = [False] * n
#     network_count = 0

#     for i in range(n):
#         if not visited[i]:
#             dfs(i, visited, computers)
#             network_count += 1

#     return network_count