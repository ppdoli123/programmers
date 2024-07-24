def solution(n, computers):
    def dfs(node, visited, computers):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in range(n):
                if computers[current][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    visited = [False] * n
    network_count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            network_count += 1

    return network_count