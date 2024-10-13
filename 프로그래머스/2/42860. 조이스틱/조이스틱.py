def solution(name):
    n = len(name)
    answer = 0
    min_move = n - 1

    for i, char in enumerate(name):
        # 상하 이동
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 좌우 이동
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        
        # 순방향으로 가는 경우와 뒤로 돌아가는 경우 중 최소값 선택
        min_move = min(min_move, i + i + n - next, i + 2 * (n - next))

    answer += min_move
    return answer