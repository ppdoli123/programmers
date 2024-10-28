import heapq
def solution(A, B):
    # 100000번 경기 진행 result 값은 0 부터 100000
    #같으면 0 100000 -> 100000 뒤에서부터 할까  ? 1368 2257 
    answer = 0
    B.sort()
    heapq.heapify(A)
    for i in range(len(A)):
        max_num = heapq.heappop(A)
        for e in range(len(B)):
            if max_num < B[e]:
                B.remove(B[e])
                answer += 1
                break
        if len(A) != len(B):
            B.remove(B[0])
        
    return answer