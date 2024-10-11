def solution(N, road, K):
    answer = 0
    distances = [float('inf')] * (N + 1)
    distances[1] = 0  # 1번 마을의 거리는 0으로 초기화

    memo = []
    for _ in range(N - 1):
        for start, end, time in road:
            # 양방향 도로 고려
            if distances[start] + time < distances[end]:
                distances[end] = distances[start] + time
            if distances[end] + time < distances[start]:
                distances[start] = distances[end] + time
    for i in distances[1:]:
        if i <= K:
            answer += 1
        
    return answer 

